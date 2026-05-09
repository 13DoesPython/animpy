import pytest
import animpy

def test_text_creation():
    """Test Text object creation"""
    text = animpy.Text("Hello", 10, 5, 255, 0, 0)
    assert text.text == "Hello"
    assert text.x == 10
    assert text.y == 5
    assert text.r == 255
    assert text.g == 0
    assert text.b == 0
    assert text.z_index == 0

def test_text_with_frames():
    """Test Text with multiple frames"""
    frames = ["Frame 1", "Frame 2", "Frame 3"]
    text = animpy.Text(frames, 0, 0)
    assert text.frames == frames
    assert text.text == "Frame 1"
    assert text.current_frame_idx == 0

def test_text_change_frame():
    """Test frame changing"""
    frames = ["A", "B", "C"]
    text = animpy.Text(frames, 0, 0)
    text.change_frame()
    assert text.text == "B"
    assert text.current_frame_idx == 1
    text.change_frame()
    assert text.text == "C"
    assert text.current_frame_idx == 2
    text.change_frame()  # Should wrap around
    assert text.text == "A"
    assert text.current_frame_idx == 0

def test_text_movement():
    """Test text movement methods"""
    text = animpy.Text("Test", 10, 20)
    text.moveX(5)
    assert text.x == 15
    text.moveY(-3)
    assert text.y == 17

def test_text_dimensions():
    """Test text width and height properties"""
    single_line = animpy.Text("Hello World", 0, 0)
    assert single_line.width == 11
    assert single_line.height == 1

    multi_line = animpy.Text("Line 1\nLine 2\nLine 3", 0, 0)
    assert multi_line.width == 20  # "Line 1\nLine 2\nLine 3" = 6 + 1 + 6 + 1 + 6 = 20
    assert multi_line.height == 3

def test_text_color_change():
    """Test color changing"""
    text = animpy.Text("Test", 0, 0, 255, 255, 255)
    text.change_rgb_values(100, 150, 200)
    assert text.r == 100
    assert text.g == 150
    assert text.b == 200

def test_effect_text_creation():
    """Test EffectText creation"""
    effect_text = animpy.EffectText("Effect", 5, 10, 0, 255, 0)
    assert effect_text.text == "Effect"
    assert effect_text.x == 5
    assert effect_text.y == 10
    assert effect_text.velocity_x == 0.0
    assert effect_text.velocity_y == 0.0