# Animpy Documentation

Animpy is a terminal animation library for Python. It makes it easy to animate text, particles, shapes, audio, and interactive input in terminal applications.

## What’s new in Animpy

- **PhysicsScene**: apply gravity, friction, bounce, angular motion, and directional forces.
- **EffectText**: built-in text effects such as shaking, gravity fall, decay, fade-out, smoothing, and pulsing.
- **InteractiveScene**: real-time keyboard and mouse input with callbacks, quick exit helpers, and boundary limiting.
- **Particles**: burst, emit, lifetime, and velocity-based particle effects.
- **Shapes**: create text-based rectangles, circles, and polygons.
- **Groups**: group text objects and change them together.
- **Audio**: load sound, play tracks, stop, volume control, and timed playback.

## Install

```bash
pip install animpy
```

## Quick Start

```python
import animpy

scene = animpy.Scene()
text = animpy.Text("Hello, Animpy!", 10, 5, r=255, g=100, b=50)
scene.add(text)
for _ in range(20):
    text.moveX(1)
    scene.render()
```

## Core Feature Overview

### Text

`Text` is the basic animated object in Animpy. It supports RGB color, movement, frame animation, and collision handling.

- `moveX(dx)` / `moveY(dy)` — move text horizontally or vertically.
- `centerX()` — center the text horizontally in the scene.
- `change_rgb_values(r, g, b)` — update the text color.
- `change_frame()` — cycle through multi-line text frames.
- `collides_with(other)` — detect collisions with another object.
- `on_collide_callback(other, callback)` — run code when collision happens.

### EffectText

`EffectText` extends `Text` with reusable animation effects.

```python
import animpy

effect = animpy.EffectText("Glitch", 10, 5, r=255, g=255, b=0)
effect.shaking_text(intensity=2)
```

Useful methods:

- `gravity_text(floor=20, gravity=0.5)` — simulate gravity and floor collision.
- `shaking_text(intensity=1)` — shake text randomly.
- `decaying_text(time, decay_rate=0.1)` — remove text characters as it fades.
- `fade_out_text(time, fade_rate=0.1)` — reduce color brightness over time.
- `lerp_text(target_x, target_y, t)` — smoothly interpolate toward a target.
- `pulse_text(time, pulse_rate=0.5)` — pulse brightness in a loop.

### PhysicsScene

`PhysicsScene` adds motion helpers to a normal scene.

```python
scene = animpy.PhysicsScene()
ball = animpy.EffectText("O", 40, 2, r=255, g=0, b=0)
ball.velocity_x = 1.0
ball.velocity_y = 0.0
scene.add(ball)

while True:
    scene.apply_physics(ball)
    scene.render()
```

Key physics methods:

- `apply_gravity(obj)` — make an object fall toward the floor.
- `apply_friction(obj, friction=0.1)` — slow down velocity.
- `bounce(obj, bounce_factor=0.5)` — bounce off the floor.
- `apply_physics(obj)` — combine gravity, friction, and bounce.
- `angular_motion(obj, angle, speed)` — set directional velocity.
- `push(obj, force_x, force_y)` — apply a force to an object.

### InteractiveScene

`InteractiveScene` enables keyboard and mouse-driven terminal apps.

```python
scene = animpy.InteractiveScene()
player = animpy.Text("P", 10, 10, r=0, g=255, b=255)
scene.add(player)

while True:
    if scene.key_pressed("w"):
        player.moveY(-1)
    if scene.key_pressed("esc"):
        break
    scene.render()
```

Interactive helpers:

- `key_pressed(key)`
- `key_released(key)`
- `on_key_press_callback(key, callback)`
- `on_key_release_callback(key, callback)`
- `mouse_pressed(button="left")`
- `mouse_position()`
- `on_mouse_press_callback(button, callback)`
- `mouse_release(button, callback)`
- `mouse_release_callback(button, callback)`
- `quick_exit(key="esc")`
- `quick_exit_callback(key, callback)`
- `limit_to_bounds(obj)`
- `limit_group_to_bounds(group)`

### Particles

Use `Particle` to create explosions, trails, or other visual effects.

```python
particle = animpy.Particle("*", 30, 10, r=255, g=150, b=50, lifetime=3.0)
particle.burst(scene, count=20, speed=2.0)
```

Particle methods:

- `burst(scene, count=20, speed=2.0)`
- `emit(scene)`
- `update_all(delta_time)`
- `is_dead()`

### Shapes

`Shapes` builds text-based rectangle, circle, and polygon art.

```python
rect = animpy.Shapes.rectangle(20, 5, "#")
circle = animpy.Shapes.circle(4, "*")
poly = animpy.Shapes.polygon([(0,0), (5,0), (3,4)], "*")
```

### Groups

`Group` gathers multiple text objects so they can move and change together.

```python
group = animpy.Group(text1, text2)
group.position(5, 0)
group.change_rgb_values(255, 0, 0)
```

### Audio

`Audio` adds sound to terminal applications.

```python
audio = animpy.Audio()
audio.load("bg", "music.mp3")
audio.play("bg", loop=-1)
audio.set_volume("bg", 0.5)
```

### Keychains and animation paths

Use `Keychains`, `Keyframe`, and `Coords` to move objects along a path.

```python
path = animpy.Keychains(animpy.Keyframe(10, 5), animpy.Keyframe(20, 10))
path.follow_path(text, speed=1)
```

## More documentation

- [Features](features.md) — full feature guide with examples
- [API Reference](api.md) — complete class and method reference
- [Examples](https://github.com/13DoesPython/animpy/tree/main/examples) — sample scripts you can run today

## Support

If you like Animpy, please give it a star on GitHub: https://github.com/13DoesPython/animpy
