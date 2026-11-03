import struct
import uuid
import urllib.error

from unittest.mock import patch
from triangulator import app

def create_pointset(points):
    data = struct.pack("<I", len(points))
    for x, y in points:
        data += struct.pack("<ff", x, y)
    return data

# Code 200
# Test le cas où la triangulation est créée correctement
@patch("triangulator.fetch_pointset")
def test_triangle_created(mock_fetch):
    points = [(0, 0), (1, 0), (0, 1)]
    mock_fetch.return_value = create_pointset(points)
    client = app.test_client()

    reponse = client.get(f"/triangulation/{uuid.uuid4()}")

    assert reponse.status_code == 200

    _, triangles = decode_triangles(reponse.data)
    assert len(triangles) == 1

# Code 400
# Test le cas où l'identifiant UUID est invalide
def test_invalid_uuid():
    client = app.test_client()

    reponse = client.get("/triangulation/unuuidinvalide")

    assert reponse.status_code == 400

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data

# Code 404
# Test le cas où le pointset n'est pas trouvé
@patch("triangulator.fetch_pointset")
def test_no_pointset(mock_fetch):
    mock_fetch.side_effect = urllib.error.HTTPError("", 404, "", None, None)
    client = app.test_client()

    reponse = client.get(f"/triangulation/{uuid.uuid4()}")

    assert reponse.status_code == 404

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data

# Code 500
# Test le cas où le triangle n'est pas créé
@patch("triangulator.fetch_pointset")
def test_triangle_not_created(mock_fetch):
    points = [(0, 1), (1, 1), (2, 1)]
    mock_fetch.return_value = create_pointset(points)
    client = app.test_client()
    
    reponse = client.get(f"/triangulation/{uuid.uuid4()}")

    assert reponse.status_code == 500

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data

# Test le cas où il n'y a pas assez de points
@patch("triangulator.fetch_pointset")
def test_triangle_insufficient_points(mock_fetch):
    points = [(0, 0), (1, 1)]
    mock_fetch.return_value = create_pointset(points)
    client = app.test_client()
    
    reponse = client.get(f"/triangulation/{uuid.uuid4()}")

    assert reponse.status_code == 500
    assert reponse.headers["Content-Type"] == "application/json"

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data

# Test le cas où le pointset est corrompu
@patch("triangulator.fetch_pointset")
def test_triangle_corrupted_pointset(mock_fetch):
    mock_fetch.return_value = b"\x01\x00\x00\x00\x00"
    client = app.test_client()
    
    reponse = client.get(f"/triangulation/{uuid.uuid4()}")

    assert reponse.status_code == 500

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data

# Code 503
@patch("triangulator.fetch_pointset")
def test_triangle_not_available(mock_fetch):
    mock_fetch.side_effect = urllib.error.HTTPError("", 503, "", None, None)
    client = app.test_client()
   
    reponse = client.get(f"/triangulation/{uuid.uuid4()}")
   
    assert reponse.status_code == 503

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data

# Test le cas d'une erreur réseau pendant la communication
@patch("triangulator.fetch_pointset")
def test_pointset_manager_network_error(mock_fetch):
    mock_fetch.side_effect = urllib.error.URLError("Connection refused")
    client = app.test_client()

    reponse = client.get(f"/triangulation/{uuid.uuid4()}")

    assert reponse.status_code == 503
    assert reponse.headers["Content-Type"] == "application/json"

    data = reponse.get_json()
    assert "code" in data
    assert "message" in data