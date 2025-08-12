from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from app import db
from app.models.models import Admin, Cliente

auth_bp = Blueprint('auth', __name__)

# -----------------------
# LOGIN
# -----------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        # Buscar primero en admin
        user = Admin.query.filter_by(correo=correo).first()
        tipo = "admin"

        if not user:
            # Si no es admin, buscar en cliente
            user = Cliente.query.filter_by(correo=correo).first()
            tipo = "cliente"

        if user:
            if check_password_hash(user.contrasena, contrasena):
                login_user(user)
                flash('Inicio de sesión con éxito', 'success')
                if tipo == 'admin':
                    return redirect(url_for('dashboard.admin_dashboard'))
                else:
                    return redirect(url_for('dashboard.cliente_dashboard'))
            else:
                flash('Contraseña incorrecta', 'danger')
                return redirect(url_for('auth.login'))
        else:
            flash('Correo no registrado', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

# -----------------------
# REGISTRO
# -----------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']  # cambiar aquí: el form debe mandar "nombre" o cambiar a "nombres"
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        telefono = request.form['telefono']
        tipo_usuario = request.form.get('tipo_usuario')  # admin o cliente

        if tipo_usuario not in ["admin", "cliente"]:
            flash("Tipo de usuario no válido", "danger")
            return redirect(url_for('auth.register'))

        # Verificar si el correo ya existe en la tabla correspondiente
        existente = (Admin if tipo_usuario == "admin" else Cliente).query.filter_by(correo=correo).first()

        if existente:
            flash('Ese correo ya está registrado', 'warning')
            return redirect(url_for('auth.register'))
        else:
            hashed_pass = generate_password_hash(contrasena)
            modelo_usuario = Admin if tipo_usuario == "admin" else Cliente

            nuevo_usuario = modelo_usuario(
                nombre=nombre,  # corregido a nombres para que coincida con el modelo
                correo=correo,
                contrasena=hashed_pass,
                telefono=telefono,
                fecha_hora=datetime.utcnow()
            )

            db.session.add(nuevo_usuario)
            db.session.commit()

            flash(f'{tipo_usuario.capitalize()} registrado con éxito', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

# -----------------------
# LOGOUT
# -----------------------
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))

