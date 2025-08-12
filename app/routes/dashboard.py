from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    return render_template('admin_dashboard.html', user=current_user)

@dashboard_bp.route('/cliente_dashboard')
@login_required
def cliente_dashboard():
    if current_user.rol != 'cliente':
        return "Acceso denegado", 403
    return render_template('cliente_dashboard.html', user=current_user)
