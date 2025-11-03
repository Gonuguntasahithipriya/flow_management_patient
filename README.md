# flow_management_patient
This app is to manage patient admissions (inbound) and discharges (outbound) through REST APIs with proper data validation and storage.

# Patient Inbound & Outbound Management System (Flask)

## Overview
A simple REST API that manages patient admissions (inbound) and discharges (outbound).  
Built with Flask and SQLAlchemy — ideal for hospitals or clinics managing patient flow.

## Features
- Admit new patient (`POST /api/patients/inbound`)
- List all patients (`GET /api/patients/`)
- Discharge a patient (`PUT /api/patients/outbound/<id>`)
- Uses SQLite by default; easily configurable for MySQL
- Includes sample PyTest cases

## Setup
```bash
pip install -r requirements.txt
python app.py
