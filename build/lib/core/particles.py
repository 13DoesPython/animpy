import random
import math

class Particle:
    def __init__(self, text, x, y, r=255, g=255, b=255, lifetime=1.0):
        self.text = text
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.lifetime = lifetime
        self.age = 0.0
        self.particles = []
        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def update(self, delta_time):
        self.age += delta_time
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        if self.age >= self.lifetime:
            return False
        return True

    def emit(self, scene):
        if self.age < self.lifetime:
            particle = Particle(self.text, self.x, self.y, self.r, self.g, self.b, lifetime=self.lifetime)
            scene.add(particle)
            self.particles.append(particle)
        else:
            scene.remove(self)

    def burst(self, scene, count=10, speed=1.0):
        for _ in range(count):
            angle = random.uniform(0, 360)
            velocity_x = speed * random.uniform(0.5, 1.0) * math.cos(math.radians(angle))
            velocity_y = speed * random.uniform(0.5, 1.0) * math.sin(math.radians(angle))
            particle = Particle(self.text, self.x, self.y, self.r, self.g, self.b, lifetime=self.lifetime)
            particle.velocity_x = velocity_x
            particle.velocity_y = velocity_y
            scene.add(particle)
            self.particles.append(particle)

    def change_rgb_values(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def update_all(self, delta_time):
        for particle in self.particles[:]:
            if not particle.update(delta_time):
                self.particles.remove(particle)

    def is_dead(self):
        self.particles = [p for p in self.particles if p.age < p.lifetime]
        return len(self.particles) == 0