import os, sys, time, atexit

sys.stdout.write("\033[?25l")
atexit.register(lambda: (sys.stdout.write("\033[?25h"), sys.stdout.flush()))

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

class Text:
    def __init__(self, text: str | list[str], x: int, y: int) -> None:
        self.x = x
        self.y = y

        if isinstance(text, list):
            self.text_list = text      # store the list
            self.current_frame = 0
            self.text = text[0]        # current visible text
        else:
            self.text_list = None
            self.text = text

    def moveX(self, newX: int) -> None:
        self.x = newX

    def moveY(self, newY: int) -> None:
        self.y = newY

    def change_frame(self) -> None:
        if self.text_list:
            self.current_frame = (self.current_frame + 1) % len(self.text_list)
            self.text = self.text_list[self.current_frame]

class Scene:
    def __init__(self) -> None:
        self.items = []

    def add(self, *items: Text) -> None:
        for item in items:
            self.items.append(item)

    def render(self):
        buf = []
        buf.append("\033[2J\033[H")
        for item in self.items:
            buf.append(f"\033[{item.y + 1};{item.x + 1}H{item.text}")
        sys.stdout.write("".join(buf))
        sys.stdout.flush()