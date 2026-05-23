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
 - `set_frame(index)`
 - `set_text(text)`
 - `set_position(x,y)`
 - `move_to(x,y)`
 - `set_color(r,g,b)`
 - `type_out(text, speed=0.05, scene=None)`
 - `fall(velocity, floor)`

### EffectText

Extends `Text` and adds:

- `gravity_text(floor=20, gravity=0.5)`
- `shaking_text(intensity=1)`
- `decaying_text(time, decay_rate=0.1)`
- `fade_out_text(time, fade_rate=0.1)`
- `lerp_text(target_x, target_y, t)`
- `pulse_text(time, pulse_rate=0.5)`
 - `set_velocity(vx, vy)`
 - `reset_velocity()`
 - `apply_force(fx, fy)`
 - `fade_in_text(time, fade_rate=0.1)`

### Particle

- `Particle(text, x, y, r=255, g=255, b=255, lifetime=3.0)`
- `burst(scene, count=20, speed=2.0)`
- `emit(scene)`
- `update_all(delta_time)`
- `is_dead()`
- `change_rgb_values(r, g, b)`
- `velocity_x`, `velocity_y`
 - `set_velocity(vx, vy)`
 - `apply_force(fx, fy)`
 - `set_color(r,g,b)`
 - `reset(x,y,lifetime=None)`
 - `is_alive()`

### Group

- `Group(*items)`
- `add(item)`
- `remove(item)`
- `position(dx, dy)`
- `change_rgb_values(r, g, b)`
- `change_rgb_values_one(item, r, g, b)`
 - `clear()`
 - `contains(item)`
 - `find_by_color(r,g,b)`

### Coords

Helper class for keyframe paths.

### Keyframe

Stores target positions for path animation.

### Keychains

- `Keychains(*keyframes)`
- `follow_path(obj, speed=1)`
 - `append(keyframe)`, `clear()`, `reverse_path()`, `is_complete`

## Shapes
- `Shapes.rectangle(width, height, char="#")`
- `Shapes.circle(radius, char="*")`
- `Shapes.polygon(points, char="*")`
- `Shapes.line(x1, y1, x2, y2, char="-")`
- `Shapes.heart(size, char="♥")`
- `Shapes.triangle(x1, y1, x2, y2, x3, y3, char="^")`
- `Shapes.ellipse(center_x, center_y, radius_x, radius_y, char="o")`

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
 - `clear_items()`
 - `count_items()`
 - `find_items_at(x,y)`

### PhysicsScene

- `PhysicsScene()`
- `apply_gravity(obj)`
- `apply_friction(obj, friction=0.1)`
- `bounce(obj, bounce_factor=0.5)`
- `apply_physics(obj)`
- `angular_motion(obj, angle, speed)`
- `push(obj, force_x, force_y)`
 - `set_floor(value)`, `set_gravity(value)`, `apply_wind(obj, wind_x)`

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
 - `bind_key(key, callback)`
 - `bind_mouse(button, callback)`
 - `set_wall(value)`, `set_floor_ceiling(value)`
 - `is_inside_bounds(obj)`

### Audio

- `Audio()`
- `load(name, path)`
- `play(name, loop=0)`
- `stop(name)`
- `stop_all()`
- `set_volume(name, volume)`
- `is_playing(name)`
- `play_for_time(name, duration=5.0)`
 - `pause(name)`, `resume(name)`, `fade_in(name,duration)`, `fade_out(name,duration)`

## Utility functions

- `lerp(start, end, t)`
- `hide_cursor()`
- `show_cursor()`
- `clear_screen()`
- `print_centered(text)`
- `print_with_color(text, r, g, b)`
