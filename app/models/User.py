import datetime
from app.models.models import db


class User(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.datetime.utcnow) 
    def __repr__(self):
        return f"<id={self.id},nome={self.nome}, email={self.email}, senha={self.senha}, cpf={self.cpf}>"

