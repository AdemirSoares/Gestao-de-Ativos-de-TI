class Config:

    SECRET_KEY = "gestao-ativos-ti-2026"

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost:5432/gestao_ativos"

    SQLALCHEMY_TRACK_MODIFICATIONS = False