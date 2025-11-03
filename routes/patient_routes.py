from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Patient, db

patient_bp = Blueprint("patient_bp", __name__)

@patient_bp.route("/", methods=["GET"])
def list_patients():
    patients = Patient.query.all()
    return jsonify([p.to_dict() for p in patients])

@patient_bp.route("/inbound", methods=["POST"])
def admit_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data["name"],
        age=data["age"],
        gender=data.get("gender", "N/A"),
        condition=data.get("condition", ""),
        status="Inbound",
        admitted_at=datetime.now()
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient admitted successfully", "patient": new_patient.to_dict()}), 201

@patient_bp.route("/outbound/<int:pid>", methods=["PUT"])
def discharge_patient(pid):
    patient = Patient.query.get_or_404(pid)
    patient.status = "Outbound"
    patient.discharged_at = datetime.now()
    db.session.commit()
    return jsonify({"message": "Patient discharged successfully", "patient": patient.to_dict()})
