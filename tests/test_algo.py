from unittest.mock import patch
    
# Algo
def test_not_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 1, 1) == False

def test_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 0.5, 0.5) == True

def test_point_aligned():
    assert is_point_aligned([0,1], [1, 1], [2,1]) == True

def test_point_not_aligned():
    assert is_point_aligned([0,0], [1, 1], [2,2]) == False

def test_triangle_created_3_points():
    create_triangle([0,0], [1, 1], [2,2])

def test_triangle_created_4_points():
    create_triangle([0,0], [1, 1], [2,2], [3,3])

def test_all_point_used():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)

    assert all(
        any(point in triangle for triangle in triangles)
        for point in points
    )
