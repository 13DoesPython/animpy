import animpy

scene = animpy.Scene()
text1 = animpy.Text("Hello", 0, 0, r=255, g=0, b=0)
text2 = animpy.Text("World", 4, 0, r=0, g=255, b=0)
scene.add(text1, text2)
scene.render()

print("\nCollides:", text1.collides_with(text2))