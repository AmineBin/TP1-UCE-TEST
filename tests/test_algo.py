import pytest
    
# Algo

# -- TEST DU CERCLE --
# Test le cas où le point n'est pas dans le cercle
def test_not_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 1, 1) == False

# Test le cas où le point est dans le cercle
def test_point_inside_circle():
    assert is_point_inside_circle(0, 0, 1, 0.5, 0.5) == True

# Test le cas où le point est sur le bord du cercle
def test_point_exactly_on_circle_boundary():
    assert is_point_inside_circle(0, 0, 1, 1.0, 0.0) == False

# Test le cas où le point est dans le cercle avec des coordonnées négatives
def test_point_inside_circle_negative_coords():
    assert is_point_inside_circle(-5, -5, 2, -4, -4) == True

# Test le cas où l'identifiant du point est vide
def test_point_set_id_empty():
    assert is_point_set_id_empty(None) == True

# -- TEST ALLIGNEMENT --
# Test le cas où les points ne sont pas alignés
def test_point_not_aligned():
    assert is_point_aligned([0,0], [1, 1], [2,3]) == False

# Test le cas où les points sont alignés horizontalement
def test_point_aligned_horizontal():
    assert is_point_aligned([0, 1], [1, 1], [2, 1]) == True

# Test le cas où les points sont alignés verticalement
def test_point_aligned_vertical():
    assert is_point_aligned([2, 0], [2, 5], [2, 10]) == True

# Test le cas où les points sont presque alignés avec des nombres flottants
def test_point_almost_aligned_float():
    assert is_point_aligned([0, 0], [1, 1], [2, 2.0000001]) == False

# -- TEST TRIANGULATION --
# Test le cas où un triangle est créé avec 3 points
def test_triangle_created_3_points():
    points  = [[0, 0], [1, 1], [2, 3]]
    triangles = create_triangle(points)
    assert len(triangles) == 1

# Test le cas où des triangles sont créés avec 4 points
def test_triangle_created_4_points():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)
    assert len(triangles) == 2

# Test le cas où des triangles sont créés avec 5 points
def test_triangle_created_5_points():
    points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 2]]
    triangles = create_triangle(points)
    assert len(triangles) == 3
    
# Test le cas où tous les points sont utilisés
def test_all_point_used():
    points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    triangles = create_triangle(points)

    used_index = set()
    for triangle in triangles:
        used_index.update(triangle)

    assert len(used_index) == len(points)

# -- TEST CASSÉ VOLONTAIRE --

# Test le cas où il n'y a pas assez de points
def test_triangle_not_enough_points():
    points = [[0, 0], [1, 1]]
    
    assert create_triangle(points) == []

# Test le cas où 3 points sont alignés
def test_triangle_with_3_aligned_points():
    points = [[0, 1], [1, 1], [2, 1]]
    with pytest.raises(ValueError):
        create_triangle(points)

# Test le cas où 4 points sont alignés
def test_triangle_with_4_aligned_points():
    oints = [[0, 0], [1, 1], [2, 2], [3, 3]]
    with pytest.raises(ValueError):
        create_triangle(points)

# Test le cas où des points sont en double
def test_triangle_duplicate_points():
    points = [[0, 0], [0, 0], [1, 0], [0, 1]]
    with pytest.raises(ValueError):
        create_triangle(points)

# Test le cas où les coordonnées sont très éloignées
def test_triangle_gap_coordinates():
    points = [[-1000.5, -2000.5], [1000.5, -2000.5], [0.0, 3000.0]]
    triangles = create_triangle(points)
    assert len(triangles) == 1