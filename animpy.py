import random
import os, sys, time, atexit, shutil, keyboard

def lerp(start, end, t):
    t = max(0.0, min(1.0, t)) 
    
    return start + (end - start) * t

sys.stdout.write("\033[?25l")
atexit.register(lambda: (sys.stdout.write("\033[?25h"), sys.stdout.flush()))
terminal_size = shutil.get_terminal_size()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

ANSI = {
    # Reset
    "reset": "\033[0m",

    # Regular colors
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",

    # Bright colors
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",

    # Backgrounds
    "bg_black": "\033[40m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m",

    # Bright backgrounds
    "bg_bright_black": "\033[100m",
    "bg_bright_red": "\033[101m",
    "bg_bright_green": "\033[102m",
    "bg_bright_yellow": "\033[103m",
    "bg_bright_blue": "\033[104m",
    "bg_bright_magenta": "\033[105m",
    "bg_bright_cyan": "\033[106m",
    "bg_bright_white": "\033[107m",

    # Styles
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "reverse": "\033[7m",
    "hidden": "\033[8m",
    "strikethrough": "\033[9m",
}

sys.stdout.write("\033[?25l")
atexit.register(lambda: (sys.stdout.write("\033[?25h"), sys.stdout.flush()))

from pygame import mixer

class Audio:
    def __init__(self):
        mixer.init()
        self.sounds = {}
        self.channels = {}

    def load(self, name, file_path):
        self.sounds[name] = mixer.Sound(file_path)

    def play(self, name, loop=0):
        if name in self.sounds:
            self.channels[name] = self.sounds[name].play(loops=loop)

    def stop_all(self):
        mixer.stop()
    
    def is_playing(self, name=None):
        if name is None:
            return mixer.get_busy()
        if name in self.channels:
            return self.channels[name].get_busy()
        return False
    
class Group:
    def __init__(self, *items):
        self.items = list(items)

    def add(self, *items):
        self.items.extend(items)

    def remove(self, *items):
        for item in items:
            if item in self.items:
                self.items.remove(item)

    def position(self, newx, newy):
        for item in self.items:
            item.x += newx
            item.y += newy

class Text:
    def __init__(self, text, x, y, r=255, g=255, b=255, z_index=0):
        self.frames = text if isinstance(text, list) else [text]
        self.current_frame_idx = 0
        self.text = self.frames[0]
        
        self.x, self.y = x, y
        self.r, self.g, self.b = r, g, b
        self.z_index = z_index

    def change_frame(self):
        self.current_frame_idx = (self.current_frame_idx + 1) % len(self.frames)
        self.text = self.frames[self.current_frame_idx]

    def moveX(self, newX: int) -> None:
        self.x = newX

    def moveY(self, newY: int) -> None:
        self.y = newY

    def centerX(self):
        self.x = terminal_size.columns // 2

    def centerY(self):
        self.y = terminal_size.lines // 2

    def change_rgb_values(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @property
    def width(self):
        if isinstance(self.text, list):
            return len(self.text[self.current_frame])
        return len(self.text)
    
    @property
    def height(self):
        if isinstance(self.text, list):
            return len(self.text[self.current_frame].split("\n"))
        return len(self.text.split("\n"))

    def collides_with(self, other):
        # Get bounding box of self
        self_left = self.x
        self_right = self.x + self.width
        self_top = self.y
        self_bottom = self.y + self.height

        # Get bounding box of other
        other_left = other.x
        other_right = other.x + other.width
        other_top = other.y
        other_bottom = other.y + other.height

        # Check for overlap
        return not (self_right <= other_left or 
                    self_left >= other_right or 
                    self_bottom <= other_top or 
                    self_top >= other_bottom)

    def on_collide_callback(self, other, callback):
        if self.collides_with(other):
            callback()

    def type_out(self, full_text, speed=0.1, scene=None):
        for i in range(len(full_text) + 1):
            self.text = full_text[:i] # Take the string from start to i
            if scene:
                scene.render() # Redraw the scene
            time.sleep(speed)
    
    def fall(self, velocity=1, floor=20):
        if self.y < floor:
            self.y += velocity
        else:
            self.y = floor

class Scene:
    def __init__(self) -> None:
        self.items = []
        self.bg_color_str = ""
        self.last_frame_time = time.perf_counter()
        self.offset_x = 0
        self.offset_y = 0

    def set_bg_rgb(self, r, g, b):
        self.bg_color_str = f"\033[48;2;{r};{g};{b}m"
        sys.stdout.write(self.bg_color_str)
        sys.stdout.flush()

    def add(self, *items) -> None:
        for item in items:
            if isinstance(item, Group):
                self.items.extend(item.items)
            else:
                self.items.append(item)

    def remove(self, *items: Text) -> None:
        for item in items:
            if item in self.items:
                self.items.remove(item)

    @property
    def dt(self):
        current_time = time.perf_counter()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return delta_time

    def render(self):
        buf = ["\033[H\033[J"]
        sorted_items = sorted(self.items, key=lambda i: getattr(i, 'z_index', 0))

        for item in sorted_items:
            if isinstance(item, Group):
                for sub_item in item.items:
                    ry = int(sub_item.y) + 1 + self.offset_y
                    rx = int(sub_item.x) + 1 + self.offset_x
                    pos = f"\033[{ry};{rx}H"
                    color = f"\033[38;2;{sub_item.r};{sub_item.g};{sub_item.b}m"
                    buf.append(f"{pos}{color}{sub_item.text}")
            else:
                ry = int(item.y) + 1 + self.offset_y
                rx = int(item.x) + 1 + self.offset_x

                pos = f"\033[{ry};{rx}H"
                color = f"\033[38;2;{item.r};{item.g};{item.b}m"
                buf.append(f"{pos}{color}{item.text}")

        buf.append("\033[0m")
        sys.stdout.write("".join(buf))
        sys.stdout.flush()

    def shake(self, intensity=1):
        self.offset_x = int((os.urandom(1)[0] / 255.0 - 0.5) * 2 * intensity)
        self.offset_y = int((os.urandom(1)[0] / 255.0 - 0.5) * 2 * intensity)

    def clear(self):
        print("\033[2J\033[H")

class InteractiveScene(Scene):
    def __init__(self):
        super().__init__()
        self.last_frame_time = time.perf_counter()
        self.wall = 0 or terminal_size.columns - 1
        self.floor_ceiling = 0 or terminal_size.lines - 1

    def key_pressed(self, key):
        try:
            return keyboard.is_pressed(key)
        except:
            return False
    
    @property
    def dt(self):
        current_time = time.perf_counter()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return delta_time