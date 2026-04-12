import animpy, time

scene = animpy.Scene() # Dark blue background
text_obj = animpy.Text("🚀 ANIMPY", x=2, y=2)
scene.add(text_obj)

# Define the Path (A Triangle)
path = animpy.KeyChains(
    animpy.Keyframe(animpy.Coords(30, 5)),  # Point A
    animpy.Keyframe(animpy.Coords(15, 15)), # Point B
    animpy.Keyframe(animpy.Coords(2, 2))     # Back to Start
)

# 3. THE ANIMATION LOOP
while True:
    # Tell the path to drive the object
    path.follow_path(text_obj, speed=1)
    
    # Render the frame
    scene.render()
    
    # Simple frame rate cap
    time.sleep(0.05)