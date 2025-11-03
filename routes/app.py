from flask import Flask
from db import init_db
from routes.patient_routes import patient_bp

app = Flask(__name__)

# Use SQLite (you can replace with MySQL connection string)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///patients.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)
app.register_blueprint(patient_bp, url_prefix="/api/patients")

if __name__ == "__main__":
    app.run(debug=True)
