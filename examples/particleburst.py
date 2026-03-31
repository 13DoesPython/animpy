import animpy
import time

scene = animpy.InteractiveScene()
particle = animpy.Particle("💥", 20, 10, r=255, g=0, b=0, lifetime=5.0)
particle.update_all(0.1)  # Update the particle's state
particle.burst(scene, count=20, speed=2.0)  # Emit a burst of particles

while not particle.is_dead():
    delta = scene.dt
    scene.update(delta)  # Update all particles in the scene
    scene.render()
    time.sleep(0.01)