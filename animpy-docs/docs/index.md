# Animpy

![PyPI - Version](https://img.shields.io/pypi/v/animpy?color=orange)
[![Downloads](https://static.pepy.tech/personalized-badge/animpy?period=total&units=INTERNATIONAL_SYSTEM&left_color=black&right_color=green&left_text=downloads)](https://pepy.tech/projects/animpy)
![GitHub License](https://img.shields.io/github/license/13DoesPython/animpy)

# Introduction
Make cool terminal animations without the pain. Move text around, use RGB colors, play audio, and build actual animations. Works great on modern terminals. Perfect for spicing up your terminal apps, creating fun loading screens, or just goofing around with text effects. If you like animpy please give me a star, it helps out a ton!

## Examples

### Basic & Beginner
```python
# Spinning loading indicator
scene = animpy.Scene()
text = animpy.Text(["|", "/", "-", "\\"], 0, 0)
scene.add(text)

for i in range(20):
    scene.render()
    text.change_frame()
    time.sleep(0.1)
```

- [Linear interpolation](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/lerp.py) - Learn smooth value transitions with the lerp function
- [Loading screen](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/loading.py) - Create a simple loading animation
- [The zen of python](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/zenofpython.py) - Animated text display with color effects

### Visual Effects & Particles
```python
# Random particle simulation
scene = animpy.Scene()
terminal_size = shutil.get_terminal_size()

while True:
    particle_color_set = ["*", "+", "."]
    particle_text = random.choice(particle_color_set)
    particle_x = random.randint(0, terminal_size.columns)
    particle_y = random.randint(0, terminal_size.lines)
    
    particle = animpy.Text(particle_text, particle_x, particle_y)
    scene.add(particle)
    scene.render()
    time.sleep(0.1)
    vx = random.choice([-1, 0, 1])
    vy = random.choice([-1, 0, 1])
    particle.moveX((particle_x + vx) % terminal_size.columns)
    particle.moveY((particle.y + vy) % terminal_size.lines)
``` 
**This dates back to version 1.0.0, this method of creating particles is still valid but the new Particle class provides a more robust and efficient way to create particle effects with velocity and lifetime management. The above code is a simple example of how you could create a particle simulation using just Text objects, but for more complex effects, the Particle class is recommended.**

- [Particle simulation](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/particlesim.py) - Advanced particle system with bursts and velocity
- [Collision example](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/collision.py) - Detect and handle text collisions

### Interactive & Games
```python
# Two-player tag game with collision detection
scene = animpy.InteractiveScene()
player1 = animpy.Text("P1", 10, 10, r=255, g=255, b=0)
player2 = animpy.Text("P2", 30, 10, r=0, g=255, b=255)
scene.add(player1)
scene.add(player2)

while True:
    if scene.key_pressed("w"): y -= speed * scene.dt
    if scene.key_pressed("s"): y += speed * scene.dt
    if scene.key_pressed("a"): x -= speed * scene.dt
    if scene.key_pressed("d"): x += speed * scene.dt
    
    player1.moveX(x), player1.moveY(y)
    player2.moveX(x2), player2.moveY(y2)
    
    if player1.collides_with(player2):
        print("💥 COLLISION! Game Over.")
        break
    
    scene.render()
    time.sleep(0.01)
```

- [Player Controls](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/playercontrol.py) - Real-time keyboard input with movement and boundaries
- [Tag game](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/taggame.py) - Interactive tag game with collision detection
- [Audio example](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/audio.py) - Load and play background music with effects

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

## Comparison to other libraries

| Feature                | Animpy         | Curses          | Blessings       | Rich            |
|------------------------|----------------|-----------------|-----------------|-----------------|
| Animated text          | ✅              | ❌               | ❌               | ❌               |
| RGB color support      | ✅              | ❌               | ❌               | ✅               |
| Audio playback         | ✅              | ❌               | ❌               | ❌               |
| Easy to use            | ✅              | ❌               | ❌               | ✅               |
| Performance on modern terminals | ✅              | ✅               | ✅               | ✅               |
| Interactive input handling | ✅              | ✅               | ✅               | ✅               |
| Open source            | ✅              | ✅               | ✅               | ✅               |
| Actively maintained       | ✅              | ❌               | ❌               | ✅               |
| Python 3 support       | ✅              | ✅               | ✅               | ✅               |
| Cross-platform support   | ✅              | ✅               | ✅               | ✅               |
| Animation effects       | ✅              | ❌               | ❌               | ❌               |

### Examples of other libraries
- Curses: A low-level library for terminal handling, but it doesn't support animations or RGB colors.
- Blessings: A wrapper around curses that makes it easier to use, but still lacks animation and audio features.
- Rich: A modern library for rich text and formatting in the terminal, but it doesn't support animations or audio.
- Animpy: A high-level library designed specifically for creating terminal animations with RGB colors and audio support, making it easy to create dynamic and engaging terminal applications.

### Curses example
```python  
import curses
def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.addstr(5, 10, "Hello, Curses!", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()  # Wait for key press
curses.wrapper(main)
```

### Blessings example
```python
from blessings import Terminal
term = Terminal()

print(term.move(5, 10) + term.red("Hello, Blessings!"))
```

### Rich example
```python
from rich import print
print("[red]Hello, Rich![/red]")
```

### Animpy example
```python
import animpy
scene = animpy.Scene()
text = animpy.Text("Hello, Animpy!", 10, 5, r=255, g=100, b=50)
scene.add(text)
scene.render()
```

## Pros and Cons

### Pros
- Easy to create animated text with RGB colors
- Built-in audio support for adding sound effects and music
- Simple API for moving text and creating animations
- Works well on modern terminals with good performance

### Cons
- May not work properly on older terminals that lack RGB support
- Limited to text-based animations (no images or graphics)
- Performance may degrade with a large number of animated objects
- Still in early development, so some features may be missing or buggy

## Performance
Animpy is designed to be efficient and runs smoothly on modern terminals. The performance will depend on the complexity of the animation and the capabilities of the terminal, but in general, it should be able to handle multiple animated text objects without significant lag. For best performance, it's recommended to keep the number of animated objects reasonable and to use the `dt` property for smooth movement based on frame timing. Future improvements could include optimizing the rendering loop and adding support for more complex animations while maintaining good performance. 

## Todo list for future improvements
- Add support for sprite sheets and more complex animations
- Optimize rendering for better performance with many animated objects
- Add more built-in animation effects (e.g., fade in/out, bounce)
- Add more types of terminal items (e.g: loading bars, panels, etc)

# Usage

## Extended info for all features

**Text Class** – The foundation of Animpy's animation capabilities. Create animated text objects with full RGB color support, position control, and collision detection. Move text horizontally (`moveX`) or vertically (`moveY`), center it on screen (`centerX`), change colors dynamically (`change_rgb_values`), and detect collisions with other text objects (`collides_with`). Create typewriter effects (`type_out`), make text fall with gravity (`fall`), and cycle through multiple frames for sprite-like animations (`change_frame`). Each text object supports z-index layering for depth control and callback functions for collision events.

**Particle Class** – A complete particle effects system for creating dynamic visual effects. Each particle has a configurable lifetime, RGB color, and velocity properties for realistic motion. The `burst()` method creates multiple particles that scatter in all directions with random angles and configurable speed - perfect for explosion effects. The `emit()` method creates single particles with parent properties. Particles move based on velocity_x and velocity_y properties, automatically updating their position each frame. The `update_all()` method advances all particle animations, and `is_dead()` checks when all particles have expired. Particles support all the color manipulation methods like regular text objects.

**EffectText Class** – An extension of the Text class that includes built-in support for various text effects. Use `shake_text()` to randomly shake the text within a certain intensity, `gravity_text()` to simulate gravity with velocity and floor collision, and `decaying_text()` to create a text that fades out and disappears after a certain lifetime. This class is ideal for adding dynamic effects to your text animations without needing to manually implement the logic for each effect.

**Group Class** – Organize multiple text objects and manage them as a single unit. Add (`add`) or remove (`remove`) text objects from groups at any time. Move the entire group with `position()` to shift all members together. Change the color of all group members simultaneously with `change_rgb_values()`, or change individual items with `change_rgb_values_one()`. This is useful for creating menus, UI elements, or any cohesive visual arrangements that need to move or change appearance together.

**Coords, Keyframe, and Keychains** - Help in making a text obj follow a specific path. Only one method is there and its `follow_path` for making text follow a path and controlling speed of path movement

**Scene Class** – The core rendering engine that displays all content to the terminal. Add multiple items (`add`) to the scene including text, particles, and groups. Remove items when they're no longer needed (`remove`). Call `render()` every frame to draw everything to the terminal with proper z-index layering. The `update()` method automatically updates all particles in the scene and removes expired ones. Set background colors with `set_bg_rgb()` for immersive visuals. Create dramatic effects with `shake()`, clear the screen with `clear()`, and use the `dt` property for frame-time-based smooth animations.

**Interactive Scene Class** – An extended scene with real-time keyboard input handling. Inherits all Scene functionality and adds `key_pressed()` method to detect which keys the user is currently pressing. Provides `wall` and `floor_ceiling` properties that return the terminal boundaries for collision detection and movement constraints. Perfect for games, interactive applications, and real-time responsive animations that react to user input.

**Audio Class** – Complete audio management system for sound effects and music. Load audio files with `load()`, giving each track a unique name for reference. Play tracks with optional looping using `play()`. Control audio playback with `stop()` for specific tracks and `stop_all()` for everything. Adjust volume with `set_volume()` to create dynamic audio mixing. Check if tracks are playing with `is_playing()`, and play sounds for specific durations with `play_for_time()` for timed effects.

**Utility Functions** – `lerp()` provides linear interpolation for smooth value transitions between start and end points based on a time parameter (0 to 1). `hide_cursor()` hides the terminal cursor for cleaner animations, and `show_cursor()` shows it again when needed.

## Methods list
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
particle = animpy.Particle("#", 10, 5, r=255, g=100, b=50, lifetime=3.0)
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
scene = animpy.Scene()
scene.add(text1, text2, text3)
scene.remove(text2)  # Remove text2 from the scene
scene.render()
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

## Method instructions
Here are the instructions for all the methods in animpy, with code examples.

### **Text** – Create animated text:

#### `animpy.Text()` - Create a text object with optional RGB color and z-index for layering:
```python
text = animpy.Text("Hi", 0, 0, r=255, g=0, b=0, z_index=1)
```

#### `moveX` and `moveY` - Move text horizontally or vertically:
```python
text.moveX(10)  # Move right
text.moveY(5)   # Move down
```

#### `centerX` - Center text horizontally on the scene:
```python
text.centerX()
```

#### `change_rgb_values` - Change the text color:
```python
text.change_rgb_values(0, 255, 0)  # Change color to green
```

#### `collides_with` - Check if this text collides with another text:
```python
text.collides_with(other_text)
```

#### `on_collide_callback` - Set a callback function to be called when this text collides with another text:
```python
text.on_collide_callback(other_text, callback)
```

#### `width` and `height` - Get the dimensions of the text:
```python
text.width, text.height
```

#### `type_out` - Create a typewriter effect for the text:
```python
text.type_out("Type me!", speed=0.05, scene=scene)
```

#### `fall` - Make the text fall with gravity:
```python
text.fall(velocity=2, floor=15)
```

#### `change_frame` - Cycle through frames if the text was created with a list of strings:
```python
text.change_frame()
```

### **Particle** – Create and manage particles with velocities:

#### `animpy.Particle()` - Create a new particle object with position, color, and lifetime:
```python
particle = animpy.Particle("💥", 10, 5, r=255, g=100, b=50, lifetime=3.0)
```

#### `burst()` - Emit multiple particles that scatter in all directions with random angles:
```python
particle.burst(scene, count=20, speed=2.0)  # Creates 20 particles spreading outward at speed 2.0
```

#### `emit()` - Emit a single particle with the same properties as the parent:
```python
particle.emit(scene)  # Creates one particle at the parent's position
```

#### `update_all()` - Update all emitted particles, advancing their age and position:
```python
particle.update_all(delta_time)  # Call every frame to update particles
```

#### `is_dead()` - Check if all emitted particles have expired:
```python
if particle.is_dead():
    print("All particles have expired")
```

#### `change_rgb_values` - Change the particle color:
```python
particle.change_rgb_values(0, 255, 0)  # Change to green
```

#### `velocity_x` and `velocity_y` - Set or get the particle's velocity:
```python
particle.velocity_x = 2.0  # Move 2 units right per second
particle.velocity_y = -1.5  # Move 1.5 units up per second
```

#### `update()` - Update the particle's age and position (called automatically by Scene.update()):
```python
if not particle.update(delta_time):
    # Particle has expired
    pass
```

### **EffectText** – Text with built-in effects:

#### `animpy.EffectText()` - Create a new EffectText object that extends Text with built-in effects:
```python
effect_text = animpy.EffectText("Shaky!", 10, 5)
```
#### `shake_text` - Shake the text randomly within a certain intensity:
```python
effect_text.shake_text(intensity=1)  # Shake the text with intensity 1
```
#### `gravity_text` - Simulate gravity with velocity and floor collision:
```python
effect_text.gravity_text(floor=15, gravity=0.5)  # Text will fall with gravity and stop at floor level 15
```
#### `decaying_text` - Create a text that fades out and disappears after a certain lifetime:
```python
effect_text.decaying_text(time=3.0, decay_rate=0.5)  # Text will fade out over 3 seconds
```

### **Shapes** – Create basic shapes as text:

#### `animpy.Shapes.rectangle()` - Create a rectangle shape as a string:
```python
rect = animpy.Shapes.rectangle(20, 5, "#")  # Create a rectangle 20 wide and 5 high using '#'
```
#### `animpy.Shapes.circle()` - Create a circle shape as a string:
```python
circle = animpy.Shapes.circle(4, "*")  # Create a circle with radius 4 using '*'
```
#### `animpy.Shapes.polygon()` - Create a polygon shape from a list of (x, y) points:
```python
polygon = animpy.Shapes.polygon([(0,0), (5,0), (3,4)], "*")  # Create a triangle polygon using '*'
```

### **Group** – Group multiple texts together:

#### `animpy.Group()` - Create a new group of text objects:
```python
group = animpy.Group(text1, text2, text3)
```
#### `add` and `remove` - Add or remove text objects from the group:
```python
group.add(text4)  # Add another text to the group
group.remove(text2)  # Remove text2 from the group
```
#### `position` - Move the entire group by a certain amount:
```python
group.position(5, 0)  # Move the entire group right by 5
```

#### `change_rgb_values` - Change the color of all items in the group:
```python
group.change_rgb_values(255, 0, 0)  # Change all items to red
```

#### `change_rgb_values_one` - Change the color of a single item in the group:
```python
group.change_rgb_values_one(text1, 0, 255, 0)  # Change only text1 to green
```

### `Coords` - Helper class 1 for `Keychains`

### `Keyframe` - Helper class 2 for `Keychains`

### `Keychains` - Making text follow a path:

#### `follow_path` - make a text obj follow a path:
```python
path.follow_path(obj, speed=1)
```

### **Scene** – Render everything:

#### `animpy.Scene()` - Create a new scene:
```python
scene = animpy.Scene()
```

#### `add` and `remove` - Add or remove items from the scene:
```python
scene.add(text1, text2, text3)
scene.remove(text2)
```

#### `render` - Render the scene to the terminal:
```python
scene.render()
```

#### `update` - Update all particles in the scene and remove expired ones:
```python
scene.update(delta_time)  # Call every frame to update particles
```

#### `set_bg_rgb` - Set the background color of the scene:
```python
scene.set_bg_rgb(0, 0, 255)  # Set background color to blue
```

#### `clear` - Clear the scene:
```python
scene.clear()
```

#### `shake` - Shake the scene for a dramatic effect:
```python
scene.shake(intensity=2)
```

#### `dt` - Get the time since the last frame (useful for smooth movement):
```python
scene.dt
```

### **Interactive Scene** – Handle real-time input:

#### `animpy.InteractiveScene()` - Create a new interactive scene:
```python
scene = animpy.InteractiveScene()
```

#### `key_pressed` - Check if a specific key is currently pressed:
```python
scene.key_pressed("w")  # Check if 'w' is pressed
```

#### `wall` and `floor_ceiling` - Get the coordinates of the walls and floor/ceiling for movement boundaries:
```python
scene.wall  # Get the x-coordinate of the right/left wall
scene.floor_ceiling  # Get the y-coordinate of the floor/ceiling
```
#### `mouse_pressed` - Check if a specific mouse button is currently pressed:
```python
scene.mouse_pressed("left")  # Check if left mouse button is pressed
```

#### `mouse_position` - Get the current position of the mouse cursor:
```python
scene.mouse_position()  # Get current mouse position
```

#### `key_released` - Check if a specific key was released since the last update:
```python
scene.key_released("w")  # Check if 'w' was released since last update
```

#### `on_key_press_callback` - Set a callback function that triggers when a specific key is pressed:
```python
scene.on_key_press_callback("w", callback)  # Set a callback for when 'w' is pressed
```

#### `on_key_release_callback` - Set a callback function that triggers when a specific key is released:
```python
scene.on_key_release_callback("w", callback)  # Set a callback for when 'w' is released
```

#### `on_mouse_press_callback` - Set a callback function that triggers when a specific mouse button is pressed:
```python
scene.on_mouse_press_callback("left", callback)  # Set a callback for when left mouse button is pressed
```

### **Audio** – Play sounds:

#### `animpy.Audio()` - Create a new audio manager:
```python
audio = animpy.Audio()
```

#### `load` - Load an audio file with a specific name:
```python
audio.load("bg", "music.mp3")
```

#### `play` - Play a loaded audio track, with optional looping:
```python
audio.play("bg", loop=-1)
```

#### `stop_all` - Stop all currently playing audio:
```python
audio.stop_all()
```

#### `is_playing` - Check if a specific track is currently playing:
```python
audio.is_playing("track")
```

#### `set_volume` - Set the volume of a specific audio track:
```python
audio.set_volume("bg", 0.5)  # Set volume to 50%
```

#### `stop` - Stop a specific audio track:
```python
audio.stop("bg")  # Stop the background music
```

#### `play_for_time` - Play an audio track for a specific duration:
```python
audio.play_for_time("bg", duration=5.0)  # Play for 5 seconds
```

### **Animpy (extras)** – Some extra methods for animations:

#### `lerp` - Linear interpolation between two values:
```python
animpy.lerp(start, end, t)  # Returns a value between start and end based on t (0 to 1)
```

#### `hide_cursor` - Hide the terminal cursor:
```python
animpy.hide_cursor()  # Hides the cursor for cleaner animations
```

#### `show_cursor` - Show the terminal cursor:
```python
animpy.show_cursor()  # Shows the cursor again (usually called on exit)
```

# Simple animation example:

```python
import animpy
scene = animpy.Scene()
text = animpy.Text("Hello, Animpy!", 10, 5, r=255, g=100, b=50)
scene.add(text)
for _ in range(20):
    text.moveX(1)  # Move right
    text.moveY(0.5)  # Move down
    scene.render()
```

# Conclusion
Animpy is a powerful and easy-to-use library for creating terminal animations with RGB colors and audio support. It provides a simple API for moving text, creating animations, and handling real-time input, making it a great choice for anyone looking to add some flair to their terminal applications. With good performance on modern terminals and a growing list of features, animpy is a fantastic tool for both beginners and experienced developers alike.

# Support the project
[![Sponsor 13DoesPython](https://img.shields.io/badge/Sponsor-13DoesPython-ea4aaa?style=for-the-badge&logo=github-sponsors)](https://github.com/sponsors/13DoesPython)

## Version History

### 1.8.5
- Added new `Shapes` class for creating basic shapes like rectangles and circles using text characters, methods include:
    - `rectangle(width, height, char)` for creating a rectangle shape
    - `circle(radius, char)` for creating a circle shape
    - `polygon(points, char)` for creating a polygon shape from a list of (x, y) points
- Changed rendering method to render each particle individually for better performance and visual quality

### v1.8.0
- Added new `Coords` and `Keyframe` as helper classes for `Keychains` class
- Added brand new `Keychains` class for animating with keyframes, methods include:
    - `follow_path` for making text follow a keyframe path
- Added new method `slide_to_pos` for `Text` as a helper function for `follow_path`
- Added one new example to examples folder (keyframes.py)

### v1.7.0
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