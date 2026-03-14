import os, sys, time, atexit, shutil

sys.stdout.write("\033[?25l")
atexit.register(lambda: (sys.stdout.write("\033[?25h"), sys.stdout.flush()))
terminal_size = shutil.get_terminal_size()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def addFrame():
    return "\033[2J\033[H"

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

    def load(self, name, file_path):
        self.sounds[name] = mixer.Sound(file_path)

    def play(self, name, loop=0):
        if name in self.sounds:
            self.sounds[name].play(loops=loop)

    def stop_all(self):
        mixer.stop()

class Text:
    def __init__(self, text, x, y, r=255, g=255, b=255):
        # If 'text' is a list, we store it for frames; otherwise, it's just a string
        self.frames = text if isinstance(text, list) else [text]
        self.current_frame_idx = 0
        self.text = self.frames[0] # The current string for the renderer
        
        self.x, self.y = x, y
        self.r, self.g, self.b = r, g, b

    def change_frame(self):
        """Cycles through the list of frames"""
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

    # Add this to your Text class
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

    def add(self, *items: Text) -> None:
        for item in items:
            self.items.append(item)

    def render(self):
        try:
            buf = []
            buf.append("\033[H") 
            buf.append("\033[J") 

            for item in self.items:
                color = f"\033[38;2;{item.r};{item.g};{item.b}m"
                # Standard X, Y positioning
                pos = f"\033[{int(item.y)+1};{int(item.x)+1}H"
                buf.append(f"{pos}{color}{item.text}\033[0m")
                
            sys.stdout.write("".join(buf))
            sys.stdout.flush()
        except KeyboardInterrupt:
            sys.exit()

    def clear(self):
        print("\033[2J\033[H")