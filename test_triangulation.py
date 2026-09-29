from unittest.mock import patch

# Binary
def test_binary_not_corrupted_data():
    assert encode(2) == "0010"

def test_binary_is_corrupted_data():
    assert encode(2) == "0011"

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

def get_status():
    import requests
    response = requests.get("https://api.com/status")
    return response.status_code

# Code 200
@patch("requests.get")
def test_triangle_created(mock_get):
    mock_get.return_value.status_code = 200
    assert create_triangle() == True
    assert get_status() == 200

# Code 400
@patch("requests.get")
def test_binary_value_sup_4_bytes(mock_get):
    mock_get.return_value.status_code = 400
    assert is_binary_value_sup_4_bytes("01011") == True
    assert get_status() == 400

@patch("requests.get")
def test_binary_value_inf_4_bytes(mock_get):
    mock_get.return_value.status_code = 400
    assert is_binary_value_inf_4_bytes("010") == True
    assert get_status() == 400

@patch("requests.get")
def test_nb_point_inf_3(mock_get):
    mock_get.return_value.status_code = 400
    assert check_nb_point(2) == False
    assert get_status() == 400

@patch("requests.get")
def test_point_set_invalid_valie(mock_get):
    mock_get.return_value.status_code = 400
    assert is_point_set_valid("jizj") == False
    assert get_status() == 400

# Code 404
@patch("requests.get")
def test_point_set_id_empty(mock_get):
    mock_get.return_value.status_code = 404
    assert is_point_set_id_empty(None) == True
    assert get_status() == 404

@patch("requests.get")
def test_triangle_not_created(mock_get):
    mock_get.return_value.status_code = 500
    assert create_triangle() == False
    assert get_status() == 500