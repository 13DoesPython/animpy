import animpy.animpy as animpy
import time, random
import shutil

scene = animpy.Scene()
terminal_size = shutil.get_terminal_size()

while True:
    particle_color_set = [animpy.ANSI["black"], animpy.ANSI["red"], animpy.ANSI["yellow"], animpy.ANSI["green"], animpy.ANSI["blue"], animpy.ANSI["cyan"], animpy.ANSI["magenta"], animpy.ANSI["white"]]
    particle_color = random.choice(particle_color_set)

    particle_texts = random.choice(["*", "+", "."])
    particle_text = f"{particle_color + particle_texts}"
    
    particle_x = random.randint(0, terminal_size.columns)
    particle_y = random.randint(0, terminal_size.lines)
    particle = animpy.Text(particle_text, particle_x, particle_y)
    scene.add(particle)

    scene.render()
    time.sleep(0.1)
    vx = random.choice([-1, 0, 1])
    vy = random.choice([-1, 0, 1])
    particle.moveX((particle_x + vx) % terminal_size.columns)
    particle.moveY((particle.y + vy) % terminal_size.lines)