from flask import Blueprint, render_template

# Definir el Blueprint para manejar errores
error_views = Blueprint('error', __name__)

# Manejar el error 404 (Página no encontrada)
@error_views.app_errorhandler(404)
def not_found_error_404(error):
    return render_template('error/404.html')

# Manejar el error 403 (Acceso prohibido)
@error_views.app_errorhandler(403)
def not_found_error_403(error):
    return render_template('error/403.html')
