from app import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)

    productos = db.relationship('Producto', back_populates='categoria', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Categoria {self.nombre}>'
