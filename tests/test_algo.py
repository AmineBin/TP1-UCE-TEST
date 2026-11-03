import pytest
    
# Algo

# -- TEST DU CERCLE --
def test_not_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 1, 1) == False

def test_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 0.5, 0.5) == True

def test_point_exactly_on_circle_boundary():
    assert is_point_inside_circle(0, 0, 1, 1.0, 0.0) == False

def test_point_inside_circle_negative_coords():
    assert is_point_inside_circle(-5, -5, 2, -4, -4) == True

def test_point_set_id_empty():
    assert is_point_set_id_empty(None) == True

# -- TEST ALLIGNEMENT --
def test_point_not_aligned():
    assert is_point_aligned([0,0], [1, 1], [2,3]) == False

def test_point_aligned_horizontal():
    assert is_point_aligned([0, 1], [1, 1], [2, 1]) == True

def test_point_aligned_vertical():
    assert is_point_aligned([2, 0], [2, 5], [2, 10]) == True

def test_point_almost_aligned_float():
    assert is_point_aligned([0, 0], [1, 1], [2, 2.0000001]) == False

# -- TEST TRIANGULATION --
def test_triangle_created_3_points():
    points  = [[0, 0], [1, 1], [2, 3]]
    triangles = create_triangle(points)
    assert len(triangles) == 1

def test_triangle_created_4_points():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)
    assert len(triangles) == 2

def test_triangle_created_5_points():
    points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 2]]
    triangles = create_triangle(points)
    assert len(triangles) == 3
    
def test_all_point_used():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)

    used_index = set()
    for triangle in triangles:
        used_index.update(triangle)

    assert len(used_index) == len(points)

# -- TEST CASSE VOLONTAIRE --

def test_triangle_not_enough_points():
    points = [[0, 0], [1, 1]]
    
    assert create_triangle(points) == []

def test_triangle_with_3_aligned_points():
    points = [[0, 1], [1, 1], [2, 1]]
    with pytest.raises(ValueError):
        create_triangle(points)

def test_triangle_with_4_aligned_points():
    oints = [[0, 0], [1, 1], [2, 2], [3, 3]]
    with pytest.raises(ValueError):
        create_triangle(points)

def test_triangle_duplicate_points():
    points = [[0, 0], [0, 0], [1, 0], [0, 1]]
    with pytest.raises(ValueError):
        create_triangle(points)

def test_triangle_gap_coordinates():
    points = [[-1000.5, -2000.5], [1000.5, -2000.5], [0.0, 3000.0]]
    triangles = create_triangle(points)
    assert len(triangles) == 1