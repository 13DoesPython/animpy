import pytest
import animpy

def test_group_creation():
    """Test Group object creation"""
    group = animpy.Group()
    assert group.items == []

def test_group_add():
    """Test adding items to group"""
    group = animpy.Group()
    text1 = animpy.Text("A", 0, 0)
    text2 = animpy.Text("B", 1, 1)

    group.add(text1)
    assert text1 in group.items
    assert len(group.items) == 1

    group.add(text2)
    assert text2 in group.items
    assert len(group.items) == 2

def test_group_remove():
    """Test removing items from group"""
    group = animpy.Group()
    text1 = animpy.Text("A", 0, 0)
    text2 = animpy.Text("B", 1, 1)

    group.add(text1, text2)
    assert len(group.items) == 2

    group.remove(text1)
    assert text1 not in group.items
    assert text2 in group.items
    assert len(group.items) == 1

def test_group_position():
    """Test group position method"""
    group = animpy.Group()
    text1 = animpy.Text("A", 0, 0)
    text2 = animpy.Text("B", 10, 10)

    group.add(text1, text2)
    group.position(5, 3)

    assert text1.x == 5
    assert text1.y == 3
    assert text2.x == 15
    assert text2.y == 13

def test_group_color_change():
    """Test group color changing"""
    group = animpy.Group()
    text1 = animpy.Text("A", 0, 0, 255, 255, 255)
    text2 = animpy.Text("B", 0, 0, 255, 255, 255)

    group.add(text1, text2)
    group.change_rgb_values(100, 150, 200)

    assert text1.r == 100
    assert text1.g == 150
    assert text1.b == 200
    assert text2.r == 100
    assert text2.g == 150
    assert text2.b == 200

def test_group_change_rgb_values_one():
    """Test changing color of specific item in group"""
    group = animpy.Group()
    text1 = animpy.Text("A", 0, 0, 255, 255, 255)
    text2 = animpy.Text("B", 0, 0, 255, 255, 255)

    group.add(text1, text2)
    group.change_rgb_values_one(text1, 50, 100, 150)

    assert text1.r == 50
    assert text1.g == 100
    assert text1.b == 150
    # text2 should remain unchanged
    assert text2.r == 255
    assert text2.g == 255
    assert text2.b == 255