import datetime
from app.models.models import db


class Fotos(db.Model):
    __tablename__= "fotos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cvli= db.Column(db.Integer, nullable=False)
    uri = db.Column(db.String, nullable=False)
    def __repr__(self):
        return f"<id={self.id},id_cvli={self.id_cvli}, uri={self.uri}"
