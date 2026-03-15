import animpy, time

scene = animpy.Scene()
text = animpy.Text(["|", "/", "-", "\\"], 0, 0)
scene.add(text)

for i in range(20):
    scene.render()
    text.change_frame()
    time.sleep(0.1)