import pytest
import animpy

def test_keyframe_creation():
    """Test Keyframe creation"""
    coord = animpy.Coords(10, 20)
    keyframe = animpy.Keyframe(coord)
    assert keyframe.pos == coord
    assert keyframe.pos.x == 10
    assert keyframe.pos.y == 20

def test_keychains_creation():
    """Test KeyChains creation"""
    coord1 = animpy.Coords(0, 0)
    coord2 = animpy.Coords(10, 5)
    coord3 = animpy.Coords(20, 10)

    keyframe1 = animpy.Keyframe(coord1)
    keyframe2 = animpy.Keyframe(coord2)
    keyframe3 = animpy.Keyframe(coord3)

    keychains = animpy.KeyChains(keyframe1, keyframe2, keyframe3)
    assert len(keychains.keyframe_list) == 3
    assert keychains.keyframe_list[0].pos == coord1
    assert keychains.keyframe_list[1].pos == coord2
    assert keychains.keyframe_list[2].pos == coord3

def test_keychains_follow_path():
    """Test path following functionality"""
    coord1 = animpy.Coords(5, 0)  # Start at different position
    coord2 = animpy.Coords(10, 0)

    keyframe1 = animpy.Keyframe(coord1)
    keyframe2 = animpy.Keyframe(coord2)

    keychains = animpy.KeyChains(keyframe1, keyframe2)
    text = animpy.Text("Test", 0, 0)

    # Initially should move toward first keyframe (5, 0)
    keychains.follow_path(text, speed=3)
    assert text.x == 3  # Moving toward (5, 0)

    # After reaching first keyframe, should move toward second
    text.x = 5  # Manually set to target
    text.y = 0
    keychains.follow_path(text, speed=3)
    # Should have removed first keyframe and be moving toward second
    assert len(keychains.keyframe_list) == 1