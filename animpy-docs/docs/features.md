# Features

## EffectText

`EffectText` extends `Text` with reusable animation effects and built-in velocity support.

Example:

```python
import animpy

effect = animpy.EffectText("Shaky!", 10, 5, r=255, g=255, b=0)
effect.shaking_text(intensity=2)
effect.gravity_text(floor=15, gravity=0.5)
effect.pulse_text(time=0.5, pulse_rate=0.3)
```

### EffectText methods

- `gravity_text(floor=20, gravity=0.5)` — apply gravity and stop at a floor.
- `shaking_text(intensity=1)` — jitter the text position.
- `decaying_text(time, decay_rate=0.1)` — shrink or remove characters over time.
- `fade_out_text(time, fade_rate=0.1)` — fade the text color toward black.
- `lerp_text(target_x, target_y, t)` — smoothly interpolate to a target coordinate.
- `pulse_text(time, pulse_rate=0.5)` — pulse the text brightness.

## PhysicsScene

`PhysicsScene` adds physics-based helpers to the scene.

Example:

```python
scene = animpy.PhysicsScene()
ball = animpy.EffectText("O", 40, 2, r=200, g=50, b=50)
ball.velocity_x = 1.0
ball.velocity_y = 0.0
scene.add(ball)

while True:
    scene.apply_physics(ball)
    scene.bounce(ball, bounce_factor=0.7)
    scene.render()
```

### PhysicsScene methods

- `apply_gravity(obj)` — move the object downward.
- `apply_friction(obj, friction=0.1)` — reduce velocity over time.
- `bounce(obj, bounce_factor=0.5)` — reverse vertical motion on impact.
- `apply_physics(obj)` — convenience wrapper for gravity, friction, and bounce.
- `angular_motion(obj, angle, speed)` — apply angled velocity.
- `push(obj, force_x, force_y)` — add force in x/y directions.

## InteractiveScene

`InteractiveScene` is built for real-time terminal interaction.

Example:

```python
scene = animpy.InteractiveScene()
player = animpy.Text("P", 10, 10, r=0, g=200, b=255)
scene.add(player)

while True:
    if scene.key_pressed("w"):
        player.moveY(-1)
    if scene.key_pressed("s"):
        player.moveY(1)
    if scene.key_pressed("esc"):
        break
    scene.render()
```

### InteractiveScene helpers

- `key_pressed(key)` — test whether a key is currently pressed.
- `key_released(key)` — test whether a key was released.
- `on_key_press_callback(key, callback)` — call a callback when a key is pressed.
- `on_key_release_callback(key, callback)` — call a callback when a key is released.
- `mouse_pressed(button="left")` — test mouse button state.
- `mouse_position()` — read the mouse cursor position.
- `on_mouse_press_callback(button, callback)` — callback on mouse press.
- `mouse_release(button, callback)` — callback when a mouse button is released.
- `mouse_release_callback(button, callback)` — alternate release callback helper.
- `quick_exit(key="esc")` — exit quickly when a key is pressed.
- `quick_exit_callback(key, callback)` — run a callback when a key is pressed.
- `limit_to_bounds(obj)` — keep a text object inside the scene.
- `limit_group_to_bounds(group)` — keep a group inside the scene.

## Particles

Use `Particle` objects to create bursts and visual effects.

Example:

```python
particle = animpy.Particle("*", 30, 10, r=255, g=150, b=50, lifetime=3.0)
particle.burst(scene, count=20, speed=2.0)
```

### Particle methods

- `burst(scene, count=20, speed=2.0)` — emit many particles from a point.
- `emit(scene)` — emit a single particle instance.
- `update_all(delta_time)` — advance all active particles.
- `is_dead()` — check whether a particle has finished.

## Shapes

`Shapes` provides simple text-based geometry builders.

- `Shapes.rectangle(width, height, char)`
- `Shapes.circle(radius, char)`
- `Shapes.polygon(points, char)`

## Groups

Group multiple text objects so they move and update together.

Example:

```python
group = animpy.Group(text1, text2)
group.position(5, 0)
group.change_rgb_values(255, 0, 0)
```

### Group methods

- `add(item)` — add another object.
- `remove(item)` — remove an object.
- `position(dx, dy)` — move the whole group.
- `change_rgb_values(r, g, b)` — recolor every item.
- `change_rgb_values_one(item, r, g, b)` — recolor a single item.

## Audio

Audio support lets you add sound effects and music.

Example:

```python
audio = animpy.Audio()
audio.load("bg", "music.mp3")
audio.play("bg", loop=-1)
audio.set_volume("bg", 0.5)
```

### Audio methods

- `load(name, path)` — register an audio file.
- `play(name, loop=0)` — play an audio track.
- `stop(name)` — stop a specific track.
- `stop_all()` — stop everything.
- `set_volume(name, volume)` — control volume.
- `is_playing(name)` — check whether a track is playing.
- `play_for_time(name, duration=5.0)` — play sound for a set duration.

## Keychains and paths

Use `Keychains`, `Keyframe`, and `Coords` to animate objects along a predefined route.

Example:

```python
path = animpy.Keychains(animpy.Keyframe(10, 5), animpy.Keyframe(20, 10))
path.follow_path(text, speed=1)
```

## More documentation

- [API Reference](api.md)
- [Home](index.md)

