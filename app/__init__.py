from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Aquí ya no importamos User, sino que importamos Admin y Cliente
    from app.models.models import Admin, Cliente

    @login_manager.user_loader
    def load_user(user_id):
        tipo, id_real = user_id.split("-", 1)
        if tipo == "admin":
            return Admin.query.get(int(id_real))
        elif tipo == "cliente":
            return Cliente.query.get(int(id_real))
        return None

    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.categoria import categoria_bp
    from app.routes.productos import productos_bp
    from app.routes.carrito import carrito_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(carrito_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    return app
