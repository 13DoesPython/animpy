import animpy
import time

scene = animpy.Scene()
audio = animpy.Audio()

title = animpy.Text("🎵 Now Playing: Drunk in Love 🎵", 0, 5, r=255, g=20, b=147)
title.centerX()
title.centerY()

scene.add(title)
scene.render()

audio.load("track", r"c:\Users\Samin\Downloads\Drunk in Love.mp3")
audio.play("track")

start_time = time.time()
duration = 10  # Play for 10 seconds

try:
    while audio.is_playing("track") and (time.time() - start_time) < duration:
        time.sleep(0.1)
    audio.stop_all()
    scene.clear()
    print("Music stopped!")
except KeyboardInterrupt:
    audio.stop_all()
    scene.clear()
    print("Music stopped!")
