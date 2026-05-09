import pytest
import animpy

def test_rectangle():
    """Test rectangle shape generation"""
    rect = animpy.Shapes.rectangle(3, 2, "#")
    expected = "###\n###"
    assert rect == expected

def test_circle():
    """Test circle shape generation"""
    circle = animpy.Shapes.circle(2, "*")
    lines = circle.split('\n')
    assert len(lines) == 5  # radius*2 + 1
    # Check that center has content
    assert '*' in lines[2]

def test_triangle():
    """Test triangle shape generation"""
    triangle = animpy.Shapes.triangle(0, 0, 4, 0, 2, 2, "^")
    lines = triangle.split('\n')
    assert len(lines) == 3
    assert lines[0] == "^   ^"
    assert lines[1] == "     "
    assert lines[2] == "  ^  "

def test_ellipse():
    """Test ellipse shape generation"""
    ellipse = animpy.Shapes.ellipse(0, 0, 3, 2, "o")
    lines = ellipse.split('\n')
    assert len(lines) == 5  # radius_y*2 + 1
    # Check that it contains the character
    assert 'o' in ellipse

def test_heart():
    """Test heart shape generation"""
    heart = animpy.Shapes.heart(2, "♥")
    lines = heart.split('\n')
    assert len(lines) == 5  # size*2 + 1
    assert '♥' in heart

def test_line():
    """Test line shape generation"""
    line = animpy.Shapes.line(0, 0, 4, 2, "-")
    # Should create a line from (0,0) to (4,2)
    assert '-' in line

def test_polygon():
    """Test polygon shape generation"""
    points = [animpy.Coords(0, 0), animpy.Coords(2, 0), animpy.Coords(1, 2)]
    polygon = animpy.Shapes.polygon(points, "*")
    assert '*' in polygon
    lines = polygon.split('\n')
    assert len(lines) > 0