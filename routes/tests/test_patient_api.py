import json
from app import app, db

def setup_module(module):
    with app.app_context():
        db.drop_all()
        db.create_all()

def test_admit_patient():
    client = app.test_client()
    payload = {"name": "John Doe", "age": 45, "condition": "Fever"}
    response = client.post("/api/patients/inbound", json=payload)
    assert response.status_code == 201
    assert "Patient admitted successfully" in response.get_data(as_text=True)
