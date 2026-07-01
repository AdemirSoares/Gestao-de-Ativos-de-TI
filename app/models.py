from app.database import db


class Ativo(db.Model):

    __tablename__ = "ativos"

    id = db.Column(db.Integer, primary_key=True)

    patrimonio = db.Column(db.String(50), nullable=False, unique=True)

    hostname = db.Column(db.String(100), nullable=False)

    tipo = db.Column(db.String(50), nullable=False)

    sistema = db.Column(db.String(100), nullable=False)

    responsavel = db.Column(db.String(100), nullable=True)

    status = db.Column(db.String(30), nullable=False)

    localizacao = db.Column(db.String(100), nullable=True)