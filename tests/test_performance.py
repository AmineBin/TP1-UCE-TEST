import time
import random
import pytest

from triangulator import (
    encode_pointset,
    decode_pointset,
    create_triangle
)

# Test le temps de conversion binaire avec un petit pointset
@pytest.mark.perf
def test_perf_binary_conversion_small_set():
    # Génération de 1000 points
    random.seed(10)
    points = [(random.uniform(0.0, 1000), random.uniform(0.0, 1000.0)) for _ in range(1000)]
    
    start_time = time.perf_counter()
    
    encoded = encode_pointset(points)
    decoded_points = decode_pointset(encoded)
    
    execution_time = time.perf_counter() - start_time
    
    assert len(decoded_points) == 1000
    
    assert execution_time < 0.3

# Test le temps de conversion binaire avec un pointset moyen
@pytest.mark.perf
def test_perf_binary_conversion_medium_set():
    # Génération de 50 000 points
    random.seed(10)
    points = [(random.uniform(0.0, 1000), random.uniform(0.0, 1000.0)) for _ in range(50000)]
    
    start_time = time.perf_counter()
    
    encoded = encode_pointset(points)
    decoded_points = decode_pointset(encoded)
    
    execution_time = time.perf_counter() - start_time
    
    assert len(decoded_points) == 50000
    
    assert execution_time < 0.5

# Test le temps de conversion binaire avec un grand pointset
@pytest.mark.perf
def test_perf_binary_conversion_large_set():
    # Génération de 100 000 points
    random.seed(10)
    points = [(random.uniform(0.0, 1000.0), random.uniform(0.0, 1000.0)) for _ in range(100000)]
    
    start_time = time.perf_counter()
    
    encoded = encode_pointset(points)
    decoded_points = decode_pointset(encoded)
    
    execution_time = time.perf_counter() - start_time
    
    assert len(decoded_points) == 100000
    
    assert execution_time < 1.0

# Test le temps d'exécution de l'algorithme de triangulation
@pytest.mark.perf
def test_perf_triangulation_algorithm():
    # Génération de 1 000 points aléatoires
    random.seed(10)
    points = [[random.uniform(0.0, 1000.0), random.uniform(0.0, 1000.0)] for _ in range(1000)]
    
    start_time = time.perf_counter()
    
    triangles = create_triangle(points)
    
    execution_time = time.perf_counter() - start_time
    
    assert len(triangles) > 0
    assert execution_time < 2.0