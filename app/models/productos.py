from app import db
from .categoria import Categoria  # Solo si haces uso directo de la clase

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre_marca = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    categoria = db.relationship('Categoria', back_populates='productos')

    def __repr__(self):
        return f'<Producto {self.nombre_marca}>'
