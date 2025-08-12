from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.productos import Producto
from app.models.categoria import Categoria


productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos')
def listar_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@productos_bp.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nuevo = Producto(
            nombre_Marca=request.form['nombre'],
            descripcion=request.form['descripcion'],
            precio=request.form['precio'],
            stock=request.form['stock'],
            id_categoria=request.form['categoria']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('productos.listar_productos'))
    return render_template('producto.html', categorias=categorias)
