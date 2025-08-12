from app import db
from datetime import datetime

class Carrito(db.Model):
    __tablename__ = 'carritos'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_clientes'), nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Enum('activo', 'inactivo'), default='activo')
    
    cliente = db.relationship('Cliente', backref='carritos')

