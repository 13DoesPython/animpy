import os, sys, time, atexit, shutil
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

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_panel(text, title="Panel", style="bold white on blue"):
    panel = Panel(text, title=title, style=style)
    print(panel)

def print_centered(text):
    terminal_size = shutil.get_terminal_size()
    lines = text.split("\n")
    for line in lines:
        padding = (terminal_size.columns - len(line)) // 2
        print(" " * padding + line)

def print_with_color(text, r=255, g=255, b=255):
    color_code = f"\033[38;2;{r};{g};{b}m"
    reset_code = "\033[0m"
    print(f"{color_code}{text}{reset_code}")

# Initialize terminal settings
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