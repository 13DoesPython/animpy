import animpy
import time

speed = 30 
x, y = 10.0, 10.0

scene = animpy.InteractiveScene()
player = animpy.Text("P", x, y, r=255, g=255, b=0)
scene.add(player)

while True:    
    if scene.key_pressed("w"):
        y -= speed * scene.dt
    if scene.key_pressed("s"):
        y += speed * scene.dt
    if scene.key_pressed("a"):
        x -= speed * scene.dt
    if scene.key_pressed("d"):
        x += speed * scene.dt

    player.moveX(x)
    player.moveY(y)
    scene.render()

    time.sleep(0.01)