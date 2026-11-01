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

def test_binary_negative_value():
    value = -5
    result = encode(value)
    assert decode(result) == value

def test_binary_decimal_value():
    with pytest.raises((TypeError, ValueError)):
        encode(5.3)

def test_binary_invalid_characters():
    with pytest.raises((TypeError, ValueError)):
        decode("jizj")

def test_binary_invalid_length():
    with pytest.raises((TypeError, ValueError)):
        decode("010")