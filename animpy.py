import random, math, mouse
import os, sys, time, atexit, shutil, keyboard
from typing import NamedTuple
from rich.panel import Panel

def lerp(start, end, t):
    t = max(0.0, min(1.0, t)) 
    
    return start + (end - start) * t

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

    os.system("")

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

    def set_volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def stop(self, name):
        if name in self.channels:
            self.channels[name].stop()
    
    def play_for_time(self, name, duration):
        if name in self.sounds:
            self.sounds[name].play()
            time.sleep(duration)
            self.sounds[name].stop()

class Particle:
    def __init__(self, text, x, y, r=255, g=255, b=255, lifetime=1.0):
        self.text = text
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.lifetime = lifetime
        self.age = 0.0
        self.particles = []
        self.velocity_x = 0.0
        self.velocity_y = 0.0
    
    def update(self, delta_time):
        self.age += delta_time
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        if self.age >= self.lifetime:
            return False
        return True

    def emit(self, scene):
        if self.age < self.lifetime:
            particle = Particle(self.text, self.x, self.y, self.r, self.g, self.b, lifetime=self.lifetime)
            scene.add(particle)
            self.particles.append(particle)
        else:
            scene.remove(self)

    def burst(self, scene, count=10, speed=1.0):
        for _ in range(count):
            angle = random.uniform(0, 360)
            velocity_x = speed * random.uniform(0.5, 1.0) * math.cos(math.radians(angle))
            velocity_y = speed * random.uniform(0.5, 1.0) * math.sin(math.radians(angle))
            particle = Particle(self.text, self.x, self.y, self.r, self.g, self.b, lifetime=self.lifetime)
            particle.velocity_x = velocity_x
            particle.velocity_y = velocity_y
            scene.add(particle)
            self.particles.append(particle) 

    def change_rgb_values(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def update_all(self, delta_time):
        for particle in self.particles[:]:
            if not particle.update(delta_time):
                self.particles.remove(particle)

    def is_dead(self):
        self.particles = [p for p in self.particles if p.age < p.lifetime]
        return len(self.particles) == 0

                
class Group:
    def __init__(self): 
        self.items = []

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

    def change_rgb_values(self, r, g, b):
        for item in self.items:
            item.change_rgb_values(r, g, b)

    def change_rgb_values_one(self, item, r, g, b):
        if item in self.items:
            item.change_rgb_values(r, g, b)

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
        self.x += newX

    def moveY(self, newY: int) -> None:
        self.y += newY

    def slide_to_pos(self, new_pos, speed=1):
        if self.x < new_pos.x:
            self.x += speed
        elif self.x > new_pos.x:
            self.x -= speed

        if self.y < new_pos.y:
            self.y += speed
        elif self.y > new_pos.y:
            self.y -= speed

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

class Coords(NamedTuple):
    x: int
    y: int

class Keyframe:
    def __init__(self, pos: Coords):
        self.pos = pos

class KeyChains:
    def __init__(self, *keyframes):
        self.keyframe_list = list(keyframes)

    def follow_path(self, obj, speed=1):
        if self.keyframe_list:
            target = self.keyframe_list[0].pos # Get the FIRST one
            obj.slide_to_pos(target, speed)
            
            # If we reached the target, remove it to start moving to the next
            if int(obj.x) == target.x and int(obj.y) == target.y:
                self.keyframe_list.pop(0)
class Shapes:
    @staticmethod
    def rectangle(width, height, char="#"):
        return "\n".join([char * width for _ in range(height)])
    
    @staticmethod
    def circle(radius, char="#"):
        result = []
        for y in range(-radius, radius + 1):
            row = ""
            for x in range(-radius, radius + 1):
                if x**2 + y**2 <= radius**2:
                    row += char
                else:
                    row += " "
            result.append(row)
        return "\n".join(result)
    
    @staticmethod
    def polygon(points, char="#"):
        if not points:
            return ""
        
        min_x = min(p.x for p in points)
        max_x = max(p.x for p in points)
        min_y = min(p.y for p in points)
        max_y = max(p.y for p in points)

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        grid = [[" " for _ in range(width)] for _ in range(height)]

        for point in points:
            x = point.x - min_x
            y = point.y - min_y
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = char

        return "\n".join("".join(row) for row in grid)

class Scene:
    def __init__(self) -> None:
        self.items = []
        self.bg_color_str = ""
        self.last_frame_time = time.perf_counter()
        self.offset_x = 0
        self.offset_y = 0

    def set_bg_rgb(self, r, g, b):
        self.bg_color_str = f"\033[48;2;{r};{g};{b}m"

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

    def update(self, delta_time):
        items_to_remove = []
        for item in self.items[:]:
            if isinstance(item, Particle):
                if not item.update(delta_time):
                    items_to_remove.append(item)
        for item in items_to_remove:
            self.remove(item)
            
    def render(self):
        try:
            columns, lines = os.get_terminal_size()
        except OSError:
            columns, lines = 80, 24

        # Clean grid (just characters first)
        grid = [[" " for _ in range(columns)] for _ in range(lines)]
        color_grid = [[None for _ in range(columns)] for _ in range(lines)]

        sorted_items = sorted(self.items, key=lambda i: getattr(i, 'z_index', 0))

        def draw_item(item):
            ry = round(item.y) + self.offset_y
            rx = round(item.x) + self.offset_x

            fg_color = f"\033[38;2;{item.r};{item.g};{item.b}m"

            lines_split = item.text.split("\n")

            for dy, line in enumerate(lines_split):
                for dx, char in enumerate(line):
                    draw_y = ry + dy
                    draw_x = rx + dx

                    if 0 <= draw_y < lines and 0 <= draw_x < columns:
                        grid[draw_y][draw_x] = char
                        color_grid[draw_y][draw_x] = fg_color

        for item in sorted_items:
            if isinstance(item, Group):
                for sub_item in item.items:
                    draw_item(sub_item)

            elif isinstance(item, Particle):
                if item.age < item.lifetime:
                    draw_item(item)

            else:
                draw_item(item)

        # 🧼 Build final output CLEANLY
        buf = ["\033[H"]

        for y in range(lines):
            row = []
            for x in range(columns):
                color = color_grid[y][x]
                char = grid[y][x]

                if color:
                    row.append(f"{color}{char}\033[0m")
                else:
                    row.append(char)

            buf.append("".join(row))

        sys.stdout.write("".join(buf))
        sys.stdout.flush()
        
    def shake(self, intensity=1):
        self.offset_x = int((os.urandom(1)[0] / 255.0 - 0.5) * 2 * intensity)
        self.offset_y = int((os.urandom(1)[0] / 255.0 - 0.5) * 2 * intensity)

    def clear(self):
        print("\033[2J\033[H")

class EffectText(Text):
    def __init__(self, text, x, y, r=255, g=255, b=255, z_index=0):
        super().__init__(text, x, y, r, g, b, z_index)
        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def gravity_text(self, floor=20, gravity=0.5):
        if self.y < floor:
            self.velocity_y += gravity
            self.y += self.velocity_y
        else:
            self.y = floor
            self.velocity_y = 0.0
    
    def shaking_text(self, intensity=1):
        self.x += int((os.urandom(1)[0] / 255.0 - 0.5) * 2 * intensity)
        self.y += int((os.urandom(1)[0] / 255.0 - 0.5) * 2 * intensity)

    def decaying_text(self, time, decay_rate=0.1):
        if time > decay_rate:
            self.text = self.text[:-1] if self.text else ""

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

    def mouse_pressed(self, button="left"):
        try:
            return mouse.is_pressed(button)
        except:
            return False
        
    def mouse_position(self):
        try:
            return mouse.get_position()
        except:
            return (0, 0)
        
    def key_released(self, key):
        try:
            return keyboard.is_released(key)
        except:
            return False
    
    def on_key_press_callback(self, key, callback):
        if self.key_pressed(key):
            callback()
    
    def on_key_release_callback(self, key, callback):
        if self.key_released(key):
            callback()

    def on_mouse_press_callback(self, button, callback):
        if self.mouse_pressed(button):
            callback()
    
    def mouse_release(self, button, callback):
        if not self.mouse_pressed(button):
            callback()

    def mouse_release_callback(self, button, callback):
        if not self.mouse_pressed(button):
            callback()

    @property
    def dt(self):
        current_time = time.perf_counter()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return delta_time