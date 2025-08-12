# app/models/dashboard.py

from app.models.categoria import Categoria

def obtener_datos_dashboard():
    total_categorias = Categoria.query.count()
    return {
        'total_categorias': total_categorias
    }
