# update_passwords.py
from app import create_app, db
from app.models.models import Cliente, Admin
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    # ACTUALIZAR CLIENTES
    clientes = Cliente.query.all()
    for cliente in clientes:
        # Si sabes la contraseña original (ej: "1234")
        cliente.contrasena = generate_password_hash("1234", method='pbkdf2:sha256')
    
    # ACTUALIZAR ADMINS
    admins = Admin.query.all()
    for admin in admins:
        admin.contrasena = generate_password_hash("1234", method='pbkdf2:sha256')

    db.session.commit()
    print("Contraseñas actualizadas y hasheadas correctamente.")
