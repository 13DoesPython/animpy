import pytest
import animpy

def test_particle_creation():
    """Test Particle object creation"""
    particle = animpy.Particle("★", 10, 20, 255, 100, 50, lifetime=2.0)
    assert particle.text == "★"
    assert particle.x == 10
    assert particle.y == 20
    assert particle.r == 255
    assert particle.g == 100
    assert particle.b == 50
    assert particle.lifetime == 2.0
    assert particle.age == 0.0
    assert particle.velocity_x == 0.0
    assert particle.velocity_y == 0.0

def test_particle_update():
    """Test particle update method"""
    particle = animpy.Particle("★", 0, 0, lifetime=1.0)
    particle.velocity_x = 1.0
    particle.velocity_y = 2.0

    # Should still be alive after small update
    alive = particle.update(0.5)
    assert alive == True
    assert particle.age == 0.5
    assert particle.x == 0.5
    assert particle.y == 1.0

    # Should die after lifetime exceeded
    alive = particle.update(0.6)
    assert alive == False
    assert particle.age == 1.1

def test_particle_burst():
    """Test particle burst functionality"""
    scene = animpy.Scene()
    particle = animpy.Particle("✨", 10, 10, lifetime=1.0)

    # Burst should add particles to scene
    initial_count = len(scene.items)
    particle.burst(scene, count=5, speed=2.0)

    assert len(scene.items) == initial_count + 5
    # Check that burst particles are in scene
    for item in scene.items[initial_count:]:
        assert isinstance(item, animpy.Particle)
        assert item.text == "✨"

def test_particle_color_change():
    """Test particle color changing"""
    particle = animpy.Particle("★", 0, 0)
    particle.change_rgb_values(100, 150, 200)
    assert particle.r == 100
    assert particle.g == 150
    assert particle.b == 200