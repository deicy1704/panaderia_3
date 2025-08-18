from app import db
from flask_login import UserMixin
from datetime import datetime

class Cliente(db.Model, UserMixin):
    __tablename__ = 'clientes'
    id_clientes = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena = db.Column(db.String(160), nullable=False)  # Guardar hash
    telefono = db.Column(db.String(20))
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        # Identificador único para Flask-Login
        return f"cliente-{self.id_clientes}"


class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id_admin = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena = db.Column(db.String(160), nullable=False)  # Guardar hash

    def get_id(self):
        return f"admin-{self.id_admin}"
