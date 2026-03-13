# Animpy

![PyPI - Downloads](https://img.shields.io/pypi/dm/animpy?color=blue&label=downloads)
![Windows](https://img.shields.io/badge/Windows-yes-green?logo=windows)
![Linux](https://img.shields.io/badge/Linux-yes-green?logo=linux)
![MacOS](https://img.shields.io/badge/MacOS-yes-green?logo=apple)

Animpy is a simple animation library for creating cool terminal animations. It gives you everything you need to make text-based animations with colors, movement, and frame-by-frame control. Perfect for CLI projects, games, or just having fun in the terminal!
**NOTE THAT SOME FEATURES MIGHT NOT WORK ON BASH TERMINAL, THIS WILL BE FIXED LATER ON**

![particlesim.py](https://github.com/13DoesPython/animpy/blob/main/particlesim.gif)

The particle simulator shown above was made entirely with Animpy.

## What's New in 1.3

- **Enhanced RGB Color Effects** – Improved support for vibrant RGB color animations; new examples show how to create gradient and rainbow text effects
- **Audio Support** – New Audio class for loading and playing sound effects with pygame mixer integration
- **Clean Ctrl+C Exit** – Graceful interrupt handling that cleanly exits without showing messy error messages

## What Can You Do?

- **Add colors and styling** to your terminal text (16 colors, bright versions, backgrounds, bold, underline, etc.)
- **Move text around** the screen wherever you want
- **Create frame-by-frame animations** with multiple text frames that you can cycle through
- **Build complex scenes** with multiple text elements rendered together
- **Control animations** smoothly and precisely

## Installation

Copy the `animpy` folder to your project directory and import it:

```python
import animpy
```

## Quick Start

Here's a simple example to get you started:

```python
import animpy

# Create a new scene
scene = animpy.Scene()

# Create some text at position (10, 5)
hello = animpy.Text("Hello, World!", 10, 5)

# Add it to the scene
scene.add(hello)

# Render it to the screen
scene.render()
```

## Complete Guide

### `addFrame()`

This is the simplest way to clear the terminal screen. It returns an ANSI code that clears everything and moves the cursor back to the top-left corner. Great if you're building your own animation loop.

```python
print(animpy.addFrame())  # Clears the screen
```

### Colors and Styling with `ANSI`

The `ANSI` dictionary has everything you need for styling text. Just add the code before your text and use `'reset'` to go back to normal.

**Available colors:**
- **Regular**: black, red, green, yellow, blue, magenta, cyan, white
- **Bright**: bright_black, bright_red, bright_green, bright_yellow, bright_blue, bright_magenta, bright_cyan, bright_white
- **Backgrounds**: bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_magenta, bg_cyan, bg_white
- **Bright backgrounds**: bg_bright_black, bg_bright_red, bg_bright_green, bg_bright_yellow, bg_bright_blue, bg_bright_magenta, bg_bright_cyan, bg_bright_white
- **Text styles**: bold, dim, italic, underline, blink, reverse, hidden, strikethrough

**Example:**
```python
import animpy

# Simple color example
text = animpy.ANSI['red'] + 'Error!' + animpy.ANSI['reset']
print(text)

# Combining styles
fancy = animpy.ANSI['bold'] + animpy.ANSI['bright_blue'] + 'AWESOME' + animpy.ANSI['reset']
print(fancy)
```

### The `Text` Class

This is where the animation magic happens. `Text` objects represent text that you can position and animate.

**Creating text:**
```python
# Simple static text at position (x=10, y=5)
text = animpy.Text("Hello", 10, 5)

# Or create animation frames with a list of strings
animation = animpy.Text(["Frame 1", "Frame 2", "Frame 3"], 10, 5)

# Create text with custom RGB colors (v1.1.0+)
colored_text = animpy.Text("Colorful!", 10, 5, r=255, g=100, b=50)
```

**Methods:**

- **`moveX(newX)`** – Move the text to a new X position
  ```python
  text.moveX(20)  # Move to x=20
  ```

- **`moveY(newY)`** – Move the text to a new Y position
  ```python
  text.moveY(10)  # Move to y=10
  ```

- **`centerX()`** – Center text horizontally on the screen (v1.1.0+)
  ```python
  text.centerX()  # Centers text horizontally
  ```

- **`centerY()`** – Center text vertically on the screen (v1.1.0+)
  ```python
  text.centerY()  # Centers text vertically
  ```

- **`change_frame()`** – Go to the next frame in a frame-by-frame animation (only works if you created it with a list)
  ```python
  animation.change_frame()  # Switch to the next frame
  ```

- **`change_rgb_values(r, g, b)`** – Change the text color using RGB values (v1.1.0+)
  ```python
  text.change_rgb_values(255, 0, 0)  # Change to red
  text.change_rgb_values(0, 255, 0)  # Change to green
  ```

- **`type_out(full_text, speed=0.1, scene=None)`** – Create an animated typing effect (v1.2+)
  ```python
  text.type_out("Hello World!", speed=0.05, scene=scene)  # Types out text character by character
  ```

- **`fall(velocity=1, floor=20)`** – Create gravity/falling effect for text (v1.2+)
  ```python
  text.fall(velocity=2, floor=10)  # Text falls with velocity until it hits the floor at y=10
  ```

### The `Scene` Class

A scene holds all your text elements and renders them to the screen at once.

**Creating and using:**
```python
scene = animpy.Scene()

# Add multiple text objects
text1 = animpy.Text("First", 5, 2)
text2 = animpy.Text("Second", 10, 5)

scene.add(text1, text2)

# Render everything to the screen
scene.render()
```

**Methods:**

- **`add(*items)`** – Add one or more Text objects to the scene
  ```python
  scene.add(text1, text2, text3)  # Add multiple at once
  ```

- **`render()`** – Draw all text objects to the screen in their current positions
  ```python
  scene.render()  # Shows everything on screen
  ```

### The `Audio` Class

The Audio class lets you load and play sound effects in your animations using pygame mixer.

**Creating and using:**
```python
audio = animpy.Audio()

# Load sound files
audio.load("jump", "sounds/jump.wav")
audio.load("background", "sounds/music.mp3")

# Play sounds
audio.play("jump")  # Play once
audio.play("background", loop=-1)  # Loop infinitely

# Stop all sounds
audio.stop_all()
```

**Methods:**

- **`load(name, file_path)`** – Load a sound file and give it a name
  ```python
  audio.load("explosion", "sounds/boom.wav")
  ```

- **`play(name, loop=0)`** – Play a loaded sound (loop=0 plays once, loop=-1 loops infinitely)
  ```python
  audio.play("explosion")  # Play once
  audio.play("background", loop=-1)  # Loop infinitely
  ```

- **`stop_all()`** – Stop all currently playing sounds
  ```python
  audio.stop_all()
  ```

## Full Animation Example

Here's a complete example showing how to create animations with the new v1.2 features:

```python
import animpy
import time

# Create a scene
scene = animpy.Scene()

# Create a title with type-out effect (v1.2+)
title = animpy.Text("", 5, 1, r=0, g=255, b=255)
scene.add(title)

# Type out the title
title.type_out("Animation Demo v1.2", speed=0.05, scene=scene)

# Create falling text (v1.2+)
falling_text = animpy.Text("Falling!", 10, 0, r=255, g=100, b=50)
scene.add(falling_text)

# Animate falling text
for i in range(15):
    falling_text.fall(velocity=1, floor=10)
    scene.render()
    time.sleep(0.1)

# Create animated text with frame cycling
frames = ["Moving...", "  Moving...", "    Moving..."]
moving_text = animpy.Text(frames, 1, 5)
scene.add(moving_text)

# Animation loop
for i in range(20):
    scene.render()
    moving_text.change_frame()
    time.sleep(0.2)
```

## Rainbow Text Example

Here's a fun example creating rainbow-colored text using RGB values:

```python
import animpy
import time

scene = animpy.Scene()

# Rainbow colors (RGB)
rainbow_colors = [
    (255, 0, 0),      # Red
    (255, 127, 0),    # Orange
    (255, 255, 0),    # Yellow
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (75, 0, 130),     # Indigo
    (148, 0, 211),    # Violet
]

# Create rainbow text - each character in a different color
text_str = "Rainbow!!!!!"
for i, char in enumerate(text_str):
    color = rainbow_colors[i % len(rainbow_colors)]
    char_text = animpy.Text(char, i, 0, r=color[0], g=color[1], b=color[2])
    scene.add(char_text)

# Render the rainbow text
scene.render()
time.sleep(2)
```

## License

See LICENSE for details.