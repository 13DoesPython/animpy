# Animpy 🎬

![PyPI - Version](https://img.shields.io/pypi/v/animpy?color=orange)
[![Downloads](https://static.pepy.tech/personalized-badge/animpy?period=total&units=INTERNATIONAL_SYSTEM&left_color=black&right_color=green&left_text=downloads)](https://pepy.tech/projects/animpy)
![GitHub License](https://img.shields.io/github/license/13DoesPython/animpy)

# Introduction
Make cool terminal animations without the pain. Move text around, use RGB colors, play audio, and build actual animations. Works great on modern terminals.

## Examples
- [Particle simulation](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/particlesim.py)
- [The zen of python](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/zenofpython.py)
- [Audio example](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/audio.py)
- [Loading screen](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/loading.py)
- [Tag game](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/taggame.py)
- [Collision example](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/collision.py)
- [Player Controls](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/playercontrol.py)
- [Linear interpolation](https://raw.githubusercontent.com/13DoesPython/animpy/refs/heads/main/examples/lerp.py)

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
- Add support for more complex animations (e.g., sprite sheets, particle systems)
- Implement a more robust audio system with volume control and multiple channels
- Optimize rendering for better performance with many animated objects
- Add more built-in animation effects (e.g., fade in/out, bounce)

# Usage

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

**Group** – Group multiple texts together:
```python
group = animpy.Group(text1, text2, text3)
group.add(text4)  # Add another text to the group
group.remove(text2)  # Remove text2 from the group
group.position(5, 0)  # Move the entire group right by 5
```

**Scene** – Render everything:
```python
scene = animpy.Scene()
scene.add(text1, text2, text3)
scene.remove(text2)  # Remove text2 from the scene
scene.render()
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
```

**Audio** – Play sounds:
```python
audio = animpy.Audio()
audio.load("bg", "music.mp3")
audio.play("bg", loop=-1)
audio.stop_all()
audio.is_playing("track")
```

**Animpy (extras)** – Some extra methods for animations:
```python
animpy.lerp(start, end, t)  # Linear interpolation between start and end
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

### **Animpy (extras)** – Some extra methods for animations:

#### `lerp` - Linear interpolation between two values:
```python
animpy.lerp(start, end, t)  # Returns a value between start and end based on t (0 to 1)
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

## Version History

## v1.5.5
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