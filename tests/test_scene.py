import pytest
import animpy

def test_scene_creation():
    """Test Scene object creation"""
    scene = animpy.Scene()
    assert scene.items == []
    assert scene.bg_color_str == ""
    assert scene.offset_x == 0
    assert scene.offset_y == 0

def test_scene_add_remove():
    """Test adding and removing items from scene"""
    scene = animpy.Scene()
    text1 = animpy.Text("Test1", 0, 0)
    text2 = animpy.Text("Test2", 1, 1)

    scene.add(text1)
    assert text1 in scene.items

    scene.add(text2)
    assert text2 in scene.items
    assert len(scene.items) == 2

    scene.remove(text1)
    assert text1 not in scene.items
    assert text2 in scene.items
    assert len(scene.items) == 1

def test_scene_group_handling():
    """Test scene handles groups correctly"""
    scene = animpy.Scene()
    group = animpy.Group()
    text1 = animpy.Text("A", 0, 0)
    text2 = animpy.Text("B", 1, 1)
    group.add(text1, text2)

    scene.add(group)
    # Group items should be flattened into scene.items
    assert text1 in scene.items
    assert text2 in scene.items

def test_scene_background_color():
    """Test setting background color"""
    scene = animpy.Scene()
    scene.set_bg_rgb(255, 0, 0)
    assert scene.bg_color_str == "\033[48;2;255;0;0m"

def test_physics_scene_creation():
    """Test PhysicsScene creation"""
    physics_scene = animpy.PhysicsScene()
    assert hasattr(physics_scene, 'gravity')
    assert hasattr(physics_scene, 'floor')
    assert physics_scene.gravity == 0.5

def test_coords():
    """Test Coords NamedTuple"""
    coord = animpy.Coords(5, 10)
    assert coord.x == 5
    assert coord.y == 10
    assert coord == (5, 10)