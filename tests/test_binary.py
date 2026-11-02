import pytest
import struct

from triangulator import (
    encode_pointset,
    decode_pointset,
    encode_triangles,
    decode_triangles
)

# Vérifie si l'intégrité de la valeur binaire n'est pas compromise
def test_binary_value_match():
    points = [(0.0, 0.0), (1.5, 2.5), (-3.0, 4.0)]

    value = encode_pointset(points)

    assert decode_pointset(value) == points

# Test le cas ou la valeur binaire attendu est vide
def test_binary_value_empty():
    points = []

    value = encode_pointset(points)

    assert decode_pointset(value) == points

# Test le cas ou il manque un octet
def test_binary_missing_point():
    data = struct.pack("<I", 2)
    data += struct.pack("<ff", 3.3, 4.4)
    with pytest.raises((TypeError, ValueError)):
        decode_pointset(data)

# Test le cas ou il y a un octet en trop
def test_binary_extra_byte():
    data = struct.pack("<I", 1)
    data += struct.pack("<ff", 3.3, 4.4)
    data += b"\x00"
    with pytest.raises((TypeError, ValueError)):
        decode_pointset(data)

# Test le cas ou la valeur est trop courte
def test_binary_too_short_length():
    with pytest.raises((TypeError, ValueError)):
        decode_pointset(b"\x00\x01")

# Test si la valeur binaire du triangle correspond aux points
def test_binary_triangles_match():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangle = [(0, 1, 2)]

    value = encode_triangles(points, triangle)
    decoded_points, decoded_triangles = decode_triangles(value)

    assert decoded_points == points
    assert decoded_triangles == triangle

# Test le cas ou le triangle est vide
def test_binary_triangles_empty():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangle = []

    value = encode_triangles(points, triangle)
    decoded_points, decoded_triangles = decode_triangles(value)

    assert decoded_points == points
    assert decoded_triangles == triangle

def test_binary_triangles_missing_indices():
    data = struct.pack("<I", 3)
    data += struct.pack("<ff", 0.0, 0.0)
    data += struct.pack("<ff", 1.0, 0.0)
    data += struct.pack("<ff", 0.0, 1.0)

    data += struct.pack("<I", 1)
    data += struct.pack("<II", 0, 1) 
    
    with pytest.raises((TypeError, ValueError)):
        decode_triangles(data)