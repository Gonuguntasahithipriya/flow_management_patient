from db import db

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    condition = db.Column(db.String(200))
    status = db.Column(db.String(50))   # Inbound / Outbound
    admitted_at = db.Column(db.DateTime)
    discharged_at = db.Column(db.DateTime)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
