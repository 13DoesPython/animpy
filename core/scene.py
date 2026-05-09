import os
import sys
import time
import math
from .utils import terminal_size
from .particles import Particle
from .group import Group
from .text import Text

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

class PhysicsScene(Scene):
    def __init__(self):
        super().__init__()
        self.gravity = 0.5
        self.floor = terminal_size.lines - 1

    def apply_gravity(self, obj):
        if obj.y < self.floor:
            obj.y += self.gravity
        else:
            obj.y = self.floor

    def apply_friction(self, obj, friction=0.1):
        if hasattr(obj, "velocity_x"):
            obj.velocity_x *= (1 - friction)
        if hasattr(obj, "velocity_y"):
            obj.velocity_y *= (1 - friction)

    def bounce(self, obj, bounce_factor=0.5):
        if obj.y >= self.floor:
            obj.y = self.floor
            if hasattr(obj, "velocity_y"):
                obj.velocity_y = -obj.velocity_y * bounce_factor

    def apply_physics(self, obj):
        self.apply_gravity(obj)
        self.apply_friction(obj)
        self.bounce(obj)

    def angular_motion(self, obj, angle, speed):
        radians = math.radians(angle)
        obj.velocity_x = math.cos(radians) * speed
        obj.velocity_y = math.sin(radians) * speed

    def push(self, obj, force_x, force_y):
        if hasattr(obj, "velocity_x"):
            obj.velocity_x += force_x
        if hasattr(obj, "velocity_y"):
            obj.velocity_y += force_y

class InteractiveScene(Scene):
    def __init__(self):
        super().__init__()
        self.last_frame_time = time.perf_counter()
        self.wall = 0 or terminal_size.columns - 1
        self.floor_ceiling = 0 or terminal_size.lines - 1

    def key_pressed(self, key):
        try:
            import keyboard
            return keyboard.is_pressed(key)
        except:
            return False

    def mouse_pressed(self, button="left"):
        try:
            import mouse
            return mouse.is_pressed(button)
        except:
            return False

    def mouse_position(self):
        try:
            import mouse
            return mouse.get_position()
        except:
            return (0, 0)

    def key_released(self, key):
        try:
            import keyboard
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

    def limit_to_bounds(self, obj):
        if obj.x < self.wall:
            obj.x = self.wall
        elif obj.x + obj.width > terminal_size.columns - self.wall:
            obj.x = terminal_size.columns - self.wall - obj.width

        if obj.y < self.floor_ceiling:
            obj.y = self.floor_ceiling
        elif obj.y + obj.height > terminal_size.lines - self.floor_ceiling:
            obj.y = terminal_size.lines - self.floor_ceiling - obj.height

    def quick_exit(self, key="esc"):
        if self.key_pressed(key):
            sys.exit()

    def quick_exit_callback(self, key, callback):
        if self.key_pressed(key):
            callback()

    def limit_group_to_bounds(self, group):
        for item in group.items:
            self.limit_to_bounds(item)

    @property
    def dt(self):
        current_time = time.perf_counter()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return delta_time