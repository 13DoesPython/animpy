import animpy

scene = animpy.Scene()
text = animpy.Text("Hello, World!", 10, 10, r=255, g=255, b=0)
scene.add(text)

speed = 0.5
start_color = (255, 255, 0)
end_color = (255, 0, 255)

t = 0.0

while True:
    delta = scene.dt
    r = int(animpy.lerp(start_color[0], end_color[0], t))
    g = int(animpy.lerp(start_color[1], end_color[1], t))
    b = int(animpy.lerp(start_color[2], end_color[2], t))
    
    text.r, text.g, text.b = r, g, b
    scene.render()

    t += speed * delta
    if t >= 1.0 or t <= 0.0:
        speed = -speed