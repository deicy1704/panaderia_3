from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('login.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', usuario=current_user)

@main_bp.route('/dashboard_admin')
@login_required
def dashboard_admin():
    return render_template('dashboard/admin.html', usuario=current_user)

@main_bp.route('/dashboard_clientes')
@login_required
def dashboard_cliente():
    return render_template('dashboard/clientes.html', usuario=current_user)
