import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_calculate_success():
    client = app.test_client()
    response = client.post(
        '/calculate',
        data=json.dumps({"expression": "2+3"}),
        content_type='application/json'
    )
    assert response.json["result"] == "5"

def test_calculate_error():
    client = app.test_client()
    response = client.post(
        '/calculate',
        data=json.dumps({"expression": "2/0"}),
        content_type='application/json'
    )
    assert response.json["result"] == "Error"
