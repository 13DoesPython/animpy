import math
import os
import time
from .utils import terminal_size, lerp

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

    @property
    def current_frame(self):
        return self.current_frame_idx

    def set_frame(self, index: int):
        if 0 <= index < len(self.frames):
            self.current_frame_idx = index
            self.text = self.frames[self.current_frame_idx]

    def set_text(self, text):
        self.frames = text if isinstance(text, list) else [text]
        self.current_frame_idx = 0
        self.text = self.frames[0]

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.set_position(x, y)

    def set_color(self, r, g, b):
        self.change_rgb_values(r, g, b)

    def type_out(self, text, speed=0.05, scene=None):
        self.text = ""
        for char in text:
            self.text += char
            if scene is not None:
                scene.render()
            time.sleep(speed)

    def fall(self, velocity, floor):
        if self.y < floor:
            self.y += velocity
        else:
            self.y = floor

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
        return len(self.text)

    @property
    def height(self):
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

    def fade_out_text(self, time, fade_rate=0.1):
        if time > fade_rate:
            fade_amount = int(255 * (1 - time / fade_rate))
            self.change_rgb_values(fade_amount, fade_amount, fade_amount)

    def lerp_text(self, target_x, target_y, t):
        self.x = lerp(self.x, target_x, t)
        self.y = lerp(self.y, target_y, t)

    def pulse_text(self, time, pulse_rate=0.5):
        pulse_amount = int(128 * (1 + math.sin(2 * math.pi * time / pulse_rate)) / 2)
        self.change_rgb_values(pulse_amount, pulse_amount, pulse_amount)

    def set_velocity(self, vx, vy):
        self.velocity_x = vx
        self.velocity_y = vy

    def reset_velocity(self):
        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def apply_force(self, fx, fy):
        self.velocity_x += fx
        self.velocity_y += fy

    def fade_in_text(self, time, fade_rate=0.1):
        if time < fade_rate:
            fade_amount = int(255 * (time / fade_rate))
            self.change_rgb_values(fade_amount, fade_amount, fade_amount)