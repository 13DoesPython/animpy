# Animpy

![PyPI - Downloads](https://img.shields.io/pypi/dm/animpy?color=blue&label=downloads)
![Windows](https://img.shields.io/badge/Windows-yes-green?logo=windows)
![Linux](https://img.shields.io/badge/Linux-yes-green?logo=linux)
![MacOS](https://img.shields.io/badge/MacOS-yes-green?logo=apple)

Animpy is a simple animation library for creating cool terminal animations. It gives you everything you need to make text-based animations with colors, movement, and frame-by-frame control. Perfect for CLI projects, games, or just having fun in the terminal!

![particlesim.py](https://github.com/13DoesPython/animpy/blob/main/particlesim.gif)

The particle simulator shown above was made entirely with Animpy.

## What's New in 1.1.0

- **True Color Support** – Use RGB values for millions of color combinations instead of just 16 colors
- **Centering Methods** – New `centerX()` and `centerY()` methods to easily center text on screen
- **Dynamic RGB Changes** – Change RGB colors on-the-fly with `change_rgb_values()` method

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

## Full Animation Example

Here's a complete example showing how to create a simple animation:

```python
import animpy
import time

# Create a scene
scene = animpy.Scene()

# Create animated text (multiple frames)
frames = ["Moving...", "  Moving...", "    Moving...", "      Moving..."]
moving_text = animpy.Text(frames, 1, 5)

# Create a title that stays still (with RGB color - v1.1.0+)
title = animpy.Text("Animation Demo", 5, 1, r=0, g=255, b=255)

# Create centered text (v1.1.0+)
centered = animpy.Text("Centered Text", 0, 10, r=255, g=100, b=50)
centered.centerX()

# Add all to the scene
scene.add(title, moving_text, centered)

# Animation loop
for i in range(20):
    scene.render()
    moving_text.change_frame()  # Next frame
    time.sleep(0.2)  # Wait 200ms
```

**NOTE THAT SOME FEATURES MIGHT NOT WORK ON BASH TERMINAL, THIS WILL BE FIXED LATER ON**

## License

See LICENSE for details.