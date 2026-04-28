# API Reference

## Classes

### Text

- `Text(text, x, y, r=255, g=255, b=255, z_index=0)`
- `moveX(value)`
- `moveY(value)`
- `centerX()`
- `change_rgb_values(r, g, b)`
- `collides_with(other)`
- `on_collide_callback(other, callback)`
- `type_out(text, speed, scene)`
- `fall(velocity, floor)`
- `change_frame()`
- `width`, `height`

### EffectText

Extends `Text` and adds:

- `gravity_text(floor=20, gravity=0.5)`
- `shaking_text(intensity=1)`
- `decaying_text(time, decay_rate=0.1)`
- `fade_out_text(time, fade_rate=0.1)`
- `lerp_text(target_x, target_y, t)`
- `pulse_text(time, pulse_rate=0.5)`

### Particle

- `Particle(text, x, y, r=255, g=255, b=255, lifetime=3.0)`
- `burst(scene, count=20, speed=2.0)`
- `emit(scene)`
- `update_all(delta_time)`
- `is_dead()`
- `change_rgb_values(r, g, b)`
- `velocity_x`, `velocity_y`

### Group

- `Group(*items)`
- `add(item)`
- `remove(item)`
- `position(dx, dy)`
- `change_rgb_values(r, g, b)`
- `change_rgb_values_one(item, r, g, b)`

### Coords

Helper class for keyframe paths.

### Keyframe

Stores target positions for path animation.

### Keychains

- `Keychains(*keyframes)`
- `follow_path(obj, speed=1)`

### Scene

- `Scene()`
- `add(*items)`
- `remove(item)`
- `render()`
- `update(delta_time)`
- `set_bg_rgb(r, g, b)`
- `clear()`
- `shake(intensity=2)`
- `dt`

### PhysicsScene

- `PhysicsScene()`
- `apply_gravity(obj)`
- `apply_friction(obj, friction=0.1)`
- `bounce(obj, bounce_factor=0.5)`
- `apply_physics(obj)`
- `angular_motion(obj, angle, speed)`
- `push(obj, force_x, force_y)`

### InteractiveScene

- `InteractiveScene()`
- `key_pressed(key)`
- `key_released(key)`
- `on_key_press_callback(key, callback)`
- `on_key_release_callback(key, callback)`
- `mouse_pressed(button="left")`
- `mouse_position()`
- `on_mouse_press_callback(button, callback)`
- `mouse_release(button, callback)`
- `mouse_release_callback(button, callback)`
- `limit_to_bounds(obj)`
- `limit_group_to_bounds(group)`
- `quick_exit(key="esc")`
- `quick_exit_callback(key, callback)`
- `wall`, `floor_ceiling`

### Audio

- `Audio()`
- `load(name, path)`
- `play(name, loop=0)`
- `stop(name)`
- `stop_all()`
- `set_volume(name, volume)`
- `is_playing(name)`
- `play_for_time(name, duration=5.0)`

## Utility functions

- `lerp(start, end, t)`
- `hide_cursor()`
- `show_cursor()`
