from flask import Blueprint, render_template
from app.models.carrito import Carrito
from app.models.productos import Producto

carrito_bp = Blueprint('carrito', __name__)

@carrito_bp.route('/carrito')
def ver_carrito():
    carrito = Carrito.query.all()
    return render_template('carrito.html', carrito=carrito)

@carrito_bp.route('/productos')
def ver_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)



