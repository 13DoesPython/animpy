import animpy
import time

speed = 25 

x, y = 10.0, 10.0
x2, y2 = 30.0, 10.0

scene = animpy.InteractiveScene()

player = animpy.Text("P1", x, y, r=255, g=255, b=0)
player2 = animpy.Text("P2", x2, y2, r=0, g=255, b=255)

scene.add(player)
scene.add(player2)

while True:
    delta = scene.dt

    if scene.key_pressed("w"): y -= speed * delta
    if scene.key_pressed("s"): y += speed * delta
    if scene.key_pressed("a"): x -= speed * delta
    if scene.key_pressed("d"): x += speed * delta
    
    if scene.key_pressed("up"):    y2 -= speed * delta
    if scene.key_pressed("down"):  y2 += speed * delta
    if scene.key_pressed("left"):  x2 -= speed * delta
    if scene.key_pressed("right"): x2 += speed * delta

    player.moveX(x), player.moveY(y)
    player2.moveX(x2), player2.moveY(y2)

    if player.collides_with(player2):
        scene.clear()
        print("💥 COLLISION! Game Over.")
        break

    scene.render()
    time.sleep(0.01) 