from flask import Blueprint, render_template
from flask_login import login_required
from app.models.categoria import Categoria

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/categoria')
@login_required
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template('categoria.html', categorias=categorias)

def obtener_datos_dashboard():
    total_categorias = Categoria.query.count()
    return {
        'total_categorias': total_categorias
    }
