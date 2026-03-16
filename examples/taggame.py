import animpy
import time

x, y = 10, 10
x2, y2 = 30, 10
scene = animpy.InteractiveScene()
player = animpy.Text("P", x, y, r=255, g=255, b=0)
player2 = animpy.Text("P", x2, y2, r=255, g=255, b=0)

scene.add(player)
scene.add(player2)

while True:
    if scene.key_pressed("w"):
        y -= 1
    elif scene.key_pressed("s"):
        y += 1
    elif scene.key_pressed("a"):
        x -= 1
    elif scene.key_pressed("d"):
        x += 1

    if scene.key_pressed("up"):
        y2 -= 1
    elif scene.key_pressed("down"):
        y2 += 1
    elif scene.key_pressed("left"):
        x2 -= 1
    elif scene.key_pressed("right"):
        x2 += 1

    player.moveX(x), player.moveY(y)
    player2.moveX(x2), player2.moveY(y2)

    if player.collides_with(player2):
        scene.clear()
        break

    scene.render()
    time.sleep(0.03)