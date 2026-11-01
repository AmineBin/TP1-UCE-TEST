import pytest
import struct

from triangulator import (
    encode_pointset,
    decode_pointset,
)

def test_binary_value_match():
    points = [(0.0, 0.0), (1.5, 2.5), (-3.0, 4.0)]

    value = encode_pointset(points)

    assert decode_pointset(value) == points

def test_binary_value_empty():
    points = []

    value = encode_pointset(points)

    assert decode_pointset(value) == points

def test_binary_missing_point():
    data = struct.pack("<I", 2)
    data += struct.pack("<ff", 3.3, 4.4)
    with pytest.raises((TypeError, ValueError)):
        decode_pointset(data)

def test_binary_too_short_length():
    with pytest.raises((TypeError, ValueError)):
        decode_pointset(b"\x00\x01")