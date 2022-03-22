import datetime
from app.models.models import db


class Cvli(db.Model):
    __tablename__= "cvli"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String, nullable=False)
    hora = db.Column(db.String, nullable=False)
    ocorrido = db.Column(db.String(1000), nullable=False)
    local = db.Column(db.String(50), nullable=False)
    id_usuario= db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"<id={self.id},data={self.data}, hora={self.hora}, ocorrido={self.ocorrido}, local={self.local}"
