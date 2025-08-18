from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models.models import Admin, Cliente

auth_bp = Blueprint('auth', __name__)

# -----------------------
# LOGIN
# -----------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    print("Entrando a la ruta de login")
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')  # lo que el usuario escribió
        print(f"Correo: {correo}, Password: {password}")
        # Buscar en clientes
        user = Cliente.query.filter_by(correo=correo).first()
        print(f"Usuario encontrado: {user}")
        if not user:
            # Buscar en admins si no es cliente
            user = Admin.query.filter_by(correo=correo).first()
        print(f"Usuario hash: {check_password_hash(user.contrasena, password)}")
        print(f"Usuario encontrado: {user.contrasena}")
        print(f"Contraseña ingresada: {password}")
        print(f"Contraseña hasheada: {generate_password_hash(password, method='pbkdf2:sha256')}")
        print("----------------------------------------------------------------------")
        if user and check_password_hash(user.contrasena, password):
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.dashboard_admin'))

        else:
            flash('Correo o contraseña incorrectos', 'danger')

    return render_template('login.html')


# -----------------------
# REGISTRO
# -----------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()
        contrasena = request.form['contrasena'].strip()
        telefono = request.form['telefono'].strip()
        tipo_usuario = request.form.get('tipo_usuario')

        if tipo_usuario not in ["admin", "cliente"]:
            flash("Tipo de usuario no válido", "danger")
            return redirect(url_for('auth.register'))

        # Verificar si el correo ya existe
        modelo_usuario = Admin if tipo_usuario == "admin" else Cliente
        existente = modelo_usuario.query.filter_by(correo=correo).first()

        if existente:
            flash('Ese correo ya está registrado', 'warning')
            return redirect(url_for('auth.register'))

        # Generar hash con el mismo método para ambos tipos
        hashed_pass = generate_password_hash(contrasena, method='pbkdf2:sha256')

        nuevo_usuario = modelo_usuario(
            nombre=nombre if tipo_usuario == "cliente" else None,
            correo=correo,
            contrasena=hashed_pass,
            telefono=telefono if tipo_usuario == "cliente" else None
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
