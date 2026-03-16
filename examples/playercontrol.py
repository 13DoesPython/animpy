import animpy
import time

x, y = 10, 10
scene = animpy.InteractiveScene()
player = animpy.Text("P", x, y, r=255, g=255, b=0)
scene.add(player)
scene.render()

while True:
    if scene.key_pressed("w"):
        y -= 1
    elif scene.key_pressed("s"):
        y += 1
    elif scene.key_pressed("a"):
        x -= 1
    elif scene.key_pressed("d"):
        x += 1

    player.moveX(x), player.moveY(y)
    scene.render()
    time.sleep(0.03)