# Animpy 🎬

Make cool terminal animations without the pain. Move text around, use RGB colors, play audio, and build actual animations. Works great on modern terminals.

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
text.type_out("Type me!", speed=0.05, scene=scene)  # Type effect
text.fall(velocity=2, floor=15)  # Falling effect
text.change_frame()  # Cycle through frames (if you used a list)
```

**Scene** – Render everything:
```python
scene = animpy.Scene()
scene.add(text1, text2, text3)
scene.render()
```

**Audio** – Play sounds:
```python
audio = animpy.Audio()
audio.load("bg", "music.mp3")
audio.play("bg", loop=-1)
audio.stop_all()
```

## What's New (v1.3)
- **Cleaner output** – Animations only take a few lines
- **Audio** – Play MP3s and WAVs without freezing
- **Better colors** – Smooth RGB effects
- **No ugly errors** – Clean exit on Ctrl+C
- **Rainbow effects** – Character-by-character color cycling

Made with ❤️ by a human.
