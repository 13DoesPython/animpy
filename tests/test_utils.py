import pytest
import animpy

def test_lerp():
    """Test linear interpolation function"""
    assert animpy.lerp(0, 10, 0.5) == 5.0
    assert animpy.lerp(0, 100, 0.2) == 20.0
    assert animpy.lerp(10, 20, 0) == 10.0
    assert animpy.lerp(10, 20, 1) == 20.0

def test_terminal_size():
    """Test that terminal size is available"""
    assert hasattr(animpy, 'terminal_size')
    assert animpy.terminal_size.columns > 0
    assert animpy.terminal_size.lines > 0

def test_ansi_colors():
    """Test ANSI color constants are available"""
    assert hasattr(animpy, 'ANSI')
    assert 'red' in animpy.ANSI
    assert 'blue' in animpy.ANSI
    assert 'green' in animpy.ANSI