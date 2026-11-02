import pytest
    
# Algo
def test_not_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 1, 1) == False

def test_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 0.5, 0.5) == True

def test_point_set_id_empty():
    assert is_point_set_id_empty(None) == True

def test_triangle_with_aligned_points():
    points = [[0,1], [1, 1], [2,1]]
    with pytest.raises(ValueError):
        create_triangle(points)

def test_point_not_aligned():
    assert is_point_aligned([0,0], [1, 1], [2,3]) == False

def test_triangle_created_3_points():
    points  = [[0, 0], [1, 1], [2, 3]]
    triangles = create_triangle(points)
    assert len(triangles) == 1

def test_triangle_created_4_points():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)
    assert len(triangles) == 2

def test_all_point_used():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)

    assert all(
        any(point in triangle for triangle in triangles)
        for point in points
    )

# Tester  si les traits ne donnent pas de triangle

# Tester assert create_triangle() == False