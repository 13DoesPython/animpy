# Animpy

![PyPI - Version](https://img.shields.io/pypi/v/animpy?color=orange)
[![Downloads](https://static.pepy.tech/personalized-badge/animpy?period=total&units=INTERNATIONAL_SYSTEM&left_color=black&right_color=green&left_text=downloads)](https://pepy.tech/projects/animpy)
![GitHub License](https://img.shields.io/github/license/13DoesPython/animpy)

Make cool terminal animations without the pain. Move text around, use RGB colors, play audio, and build actual animations. Animpy is meant for utilizing the terminal in many many different ways. There is even a feature where you can make your own minigames right in the terminal! Works great on modern terminals. If you like this please star my project, it helps out a ton!

## Examples

### Basic & Beginner
- [Linear interpolation](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/lerp.py) - Learn smooth value transitions with the lerp function
- [Loading screen](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/loading.py) - Create a simple loading animation
- [The zen of python](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/zenofpython.py) - Animated text display with color effects

### Visual Effects & Particles
- [Collision example](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/collision.py) - Detect and handle text collisions

### Interactive & Games
- [Player Controls](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/playercontrol.py) - Real-time keyboard input with movement and boundaries
- [Tag game](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/taggame.py) - Interactive tag game with collision detection
- [Audio example](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/audio.py) - Load and play background music with effects

And many more!

## Install
```bash
pip install animpy
```

## Quick Start
```python
import animpy

scene = animpy.Scene()
text = animpy.Text("Hello!", 10, 5, r=255, g=100, b=50)
scene.add(text)
scene.render()
```

## How It Works
**Text** – Create animated text:
```python
text = animpy.Text("Hi", 0, 0, r=255, g=0, b=0)
text.moveX(10)  # Move right
text.moveY(5)   # Move down
text.centerX()  # Center horizontally
text.change_rgb_values(0, 255, 0)  # Change color
text.collides_with(other_text)  # Check collision with another text
text.on_collide_callback(other_text, callback)  # Set a callback for when it collides with another text
text.width, text.height  # Get dimensions
text.type_out("Type me!", speed=0.05, scene=scene)  # Type effect
text.fall(velocity=2, floor=15)  # Falling effect
text.change_frame()  # Cycle through frames (if you used a list)
```

**Particle** – Create and manage particles with velocities:
```python
particle = animpy.Particle("💥", 10, 5, r=255, g=100, b=50, lifetime=3.0)
particle.burst(scene, count=20, speed=2.0)  # Emit burst of particles in all directions
particle.emit(scene)  # Emit a single particle
particle.change_rgb_values(0, 255, 0)  # Change particle color
particle.update_all(delta_time)  # Update all emitted particles
particle.is_dead()  # Check if all particles have expired
particle.velocity_x, particle.velocity_y  # Set particle velocity
```

**EffectText** – Text with built-in effects:
```python
effect_text = animpy.EffectText("Shaky!", 10, 5)
effect_text.shake_text(intensity=1)  # Shake the text
effect_text.gravity_text(floor=15, gravity=0.5)  # Simulate gravity
effect_text.decaying_text(time=3.0, decay_rate=0.5)
```

**Shapes** – Create basic shapes as text:
```python
rect = animpy.Shapes.rectangle(20, 5, "#")
circle = animpy.Shapes.circle(4, "*")
box = animpy.Text(rect, 5, 3, r=100, g=200, b=255)
ball = animpy.Text(circle, 40, 10, r=255, g=120, b=120)

polygon = animpy.Shapes.polygon([(0,0), (5,0), (3,4)], "*")
triangle = animpy.Text(polygon, 20, 10, r=200, g=200, b=0)
```

**Group** – Group multiple texts together:
```python
group = animpy.Group(text1, text2, text3)
group.add(text4)  # Add another text to the group
group.remove(text2)  # Remove text2 from the group
group.position(5, 0)  # Move the entire group right by 5
group.change_rgb_values(255, 0, 0)  # Change color of all items in group to red
group.change_rgb_values_one(text1, 0, 255, 0)  # Change color of a single item in group
```

**Coords** - Helper class 1 for `Keychains`

**Keyframe** - Helper class 2 for `Keychains`

**Keychains** - Making text follow a path:
```python
path = animpy.Keychains(*keyframes)
path.follow_path(obj, speed=1)
```

**Scene** – Render everything:
```python
scene = animpy.Scene()
scene.add(text1, text2, text3)
scene.remove(text2)  # Remove text2 from the scene
scene.render()
scene.update(delta_time)  # Update all particles in the scene
scene.set_bg_rgb(0, 0, 255)  # Set background color to blue
scene.clear()
scene.shake(intensity=2)  # Shake the scene
scene.dt  # Get time since last frame (for smooth movement)
```

**Interactive Scene** – Handle real-time input:
```python
scene = animpy.InteractiveScene()
scene.add(text1, text2, text3)
scene.remove(text2)  # Remove text2 from the scene
scene.render()
scene.update(delta_time)  # Update all particles in the scene
scene.set_bg_rgb(0, 0, 255)  # Set background color to blue
scene.clear()
scene.shake(intensity=2)  # Shake the scene
scene.key_pressed("w")  # Check if 'w' is pressed
scene.dt  # Get time since last frame (for smooth movement)
scene.wall  # Get the x-coordinate of the right/left wall
scene.floor_ceiling  # Get the y-coordinate of the floor/ceiling
scene.mouse_pressed("left")  # Check if left mouse button is pressed
scene.mouse_position()  # Get current mouse position
scene.key_released("w")  # Check if 'w' was released since last update
scene.on_key_press_callback("w", callback)  # Set a callback for when 'w' is pressed
scene.on_key_release_callback("w", callback)  # Set a callback for when 'w' is released
scene.on_mouse_press_callback("left", callback)  # Set a callback for when left mouse button is pressed
```

**Audio** – Play sounds:
```python
audio = animpy.Audio()
audio.load("bg", "music.mp3")
audio.play("bg", loop=-1)
audio.set_volume("bg", 0.5)  # Set volume to 50%
audio.stop("bg")  # Stop a specific audio track
audio.stop_all()  # Stop all audio
audio.is_playing("track")  # Check if audio is playing
audio.play_for_time("bg", duration=5.0)  # Play audio for a specific duration
```

**Animpy (extras)** – Some extra methods for animations:
```python
animpy.lerp(start, end, t)  # Linear interpolation between start and end
animpy.hide_cursor()  # Hide the terminal cursor
animpy.show_cursor()  # Show the terminal cursor
```

# Support the project
[![Sponsor 13DoesPython](https://img.shields.io/badge/Sponsor-13DoesPython-ea4aaa?style=for-the-badge&logo=github-sponsors)](https://github.com/sponsors/13DoesPython)

## Version History

## v1.8.5
- Added new `Shapes` class for creating basic shapes like rectangles and circles as text objects,
    - `rectangle(width, height, char)` for creating a rectangle shape
    - `circle(radius, char)` for creating a circle shape
    - `polygon(points, char)` for creating a polygon shape from a list of (x, y) points
- Changed rendering logic to support shapes as text objects, allowing you to use them like regular `Text` with position, color, and effects

## v1.8.0
- Added new `Coords` and `Keyframe` as helper classes for `Keychains` class
- Added brand new `Keychains` class for animating with keyframes, methods include:
    - `follow_path` for making text follow a keyframe path
- Added new method `slide_to_pos` for `Text` as a helper function for `follow_path`
- Added one new example to examples folder (keyframes.py)

## v1.7.0
- Added new `EffectText` class that extends `Text` with built-in support for various text effects like shaking, methods include:
    - `gravity_text(floor, gravity)` for simulating gravity with velocity and floor collision
    - `shake_text(intensity)` for shaking the text randomly within a certain intensity
    - `decaying_text(time, decay_rate)` for creating a text that fades out and disappears after a certain lifetime
- Added more mouse controls such as `mouse_released(button)` to check if a specific mouse button was released since the last update, and `mouse_release_callback(button, callback)` to set a callback function that triggers when a specific mouse button is released

### v1.6.5
- Added six new methods to interactive scene:
    - `mouse_pressed(button="left")` to check if a specific mouse button is currently pressed
    - `mouse_position()` to get the current position of the mouse cursor
    - `key_released(key)` to check if a specific key was released since the last update
    - `on_key_press_callback(key, callback)` to set a callback function that triggers when a specific key is pressed
    - `on_key_release_callback(key, callback)` to set a callback function that triggers when a specific key is released
    - `on_mouse_press_callback(button, callback)` to set a callback function that triggers when a specific mouse button is pressed

### v1.6.0
- Added new `Particle` class for creating particle effects with velocity and lifetime support
- Added `burst()` method to create particles that scatter in all directions with configurable speed
- Added `emit()` method to emit particles from a parent particle
- Added `update_all()` method to update all emitted particles
- Added `is_dead()` method to check if all particles have expired
- Added `Scene.update()` method to automatically update and remove expired particles
- Particles now support RGB color, velocity, and lifetime tracking
- Particles render individually and fade as they reach their lifetime
- Added new example for particle simulation
- Added two new methods to `Group` class: `change_rgb_values_one()` for changing color of a single item in the group, and `position()` for moving the entire group by a certain amount
- Added three new methods to `Audio` class: `is_playing()` to check if a specific audio track is currently playing, `play_for_time()` to play an audio track for a specific duration, and `stop_all()` to stop all currently playing audio tracks
- Added two new methods for the main namespace: `hide_cursor()`/`show_cursor()` for controlling the visibility of the terminal cursor during animations

### v1.5.8
- Added exclusive floor, wall, and ceiling properties to InteractiveScene for better control over movement boundaries

### v1.5.5
- Added new Group class for grouping multiple Text objects together and moving them as a unit
- Added collision detection method `on_collide_callback` to Text class for triggering callbacks when two Text objects collide

### v1.5.1
- Added full guide to project folder

### v1.5.0
- Added linear interpolation function `lerp` to `animpy` for smooth animations
- Added `dt` property to `Scene` for easy frame timing and smooth movement
- Added z-index support to `Text` for layering items in the scene
- Added scene shaking effect with `shake` method for dramatic animations

### v1.4.5
- Added background color support to `Scene` with `set_bg_rgb` method

### v1.4.1
- Added `scene.remove` method to remove items from the scene

### v1.4.0
- Added three new examples to Github example folder
- Added new class `InteractiveScene` that allows for real-time keyboard input
- Added collision detection method `collides_with` to `Text` class

### v1.3.8
- Added `audio.is_playing()` method to check if audio is currently playing
- Added two more examples to Github example folder

### v1.3.5
- Added `scene.clear` method to clear the scene
- Added version history to README

Made with ❤️ by a human.
