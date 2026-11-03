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

# Test le cas où la valeur binaire attendue est vide
def test_binary_value_empty():
    points = []

    value = encode_pointset(points)

    assert decode_pointset(value) == points

# Test si l'encodage respecte exactement le format
def test_binary_exact_format():
    points = [(1.0, 2.0), (3.0, 4.0)]

    value = encode_pointset(points)

    expected = struct.pack("<I", 2)
    expected += struct.pack("<ff", 1.0, 2.0)
    expected += struct.pack("<ff", 3.0, 4.0)
    assert value == expected

# Test le cas ou le type transmis n'est pas une liste
def test_binary_encode_invalid_type():
    with pytest.raises(TypeError):
        encode_pointset(None)

# Test le cas où un point n'a pas 2 coordonnées
def test_binary_missing_coordinate():
    points = [(1.0,)]
    with pytest.raises(ValueError):
        encode_pointset(points)

# Test le cas où les coordonnées ne sont pas des nombres
def test_binary_non_numeric_coords():
    points = [("gzer", 1.0)]
    with pytest.raises(TypeError):
        encode_pointset(points)

# Test le cas où la valeur binaire est complètement vide
def test_binary_empty():
    with pytest.raises(ValueError):
        decode_pointset(b"")

# Test le cas où il manque un octet
def test_binary_missing_point():
    data = struct.pack("<I", 2)
    data += struct.pack("<ff", 3.3, 4.4)
    with pytest.raises(ValueError):
        decode_pointset(data)

# Test le cas où il y a un octet en trop
def test_binary_extra_byte():
    data = struct.pack("<I", 1)
    data += struct.pack("<ff", 3.3, 4.4)
    data += b"\x00"
    with pytest.raises(ValueError):
        decode_pointset(data)

# Test le cas où la valeur est trop courte
def test_binary_too_short_length():
    with pytest.raises(ValueError):
        decode_pointset(b"\x00\x01")

# Test si la valeur binaire du triangle correspond aux points
def test_binary_triangles_match():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangles = [(0, 1, 2)]

    value = encode_triangles(points, triangles)
    decoded_points, decoded_triangles = decode_triangles(value)

    assert decoded_points == points
    assert decoded_triangles == triangles

# Test le cas où l'en-tête annonce trop de points
def test_binary_big_amount():
    data = struct.pack("<I", 1000)
    data += struct.pack("<ff", 1.0, 1.0)
    with pytest.raises(ValueError):
        decode_pointset(data)

# Test le cas où le triangle est vide
def test_binary_triangles_empty():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangles = []

    value = encode_triangles(points, triangles)
    decoded_points, decoded_triangles = decode_triangles(value)

    assert decoded_points == points
    assert decoded_triangles == triangles

# Test le cas où un triangle n'a pas 3 sommets
def test_binary_encode_malformed_triangle():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangles = [(0, 1)]
    with pytest.raises(ValueError):
        encode_triangles(points, triangles)

# Test le cas où un indice de triangle est hors limites
def test_binary_encode_out_of_bounds_index():
    points = [(0.0, 0.0), (1.0, 1.0)]
    triangles = [(0, 1, 5)]
    with pytest.raises(ValueError):
        encode_triangles(points, triangles)

# Test le cas où il manque un indice dans le triangle
def test_binary_triangles_missing_indices():
    data = struct.pack("<I", 3)
    data += struct.pack("<ff", 0.0, 0.0)
    data += struct.pack("<ff", 1.0, 0.0)
    data += struct.pack("<ff", 0.0, 1.0)

    data += struct.pack("<I", 1)
    data += struct.pack("<II", 0, 1) 
    
    with pytest.raises(ValueError):
        decode_triangles(data)

# Test le cas où l'indice du triangle pointe vers un sommet inexistant
def test_binary_triangles_index_out_of_range():
    data = struct.pack("<I", 3)
    data += struct.pack("<ff", 0.0, 0.0)
    data += struct.pack("<ff", 1.0, 0.0)
    data += struct.pack("<ff", 0.0, 1.0)

    data += struct.pack("<I", 1)
    data += struct.pack("<III", 0, 1, 99)
    
    with pytest.raises(ValueError):
        decode_triangles(data)