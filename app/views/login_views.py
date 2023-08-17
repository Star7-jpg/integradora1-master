from flask import Blueprint, render_template, redirect, url_for, flash, session
from models.user import User
from forms.login_forms import LoginForm

login_views = Blueprint('login', __name__)

@login_views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.nom_usuario.data
        password = form.contrasenia.data
        user = User.get_by_password(username, password)
        if not user:
            flash('Verifica tus Datos')
        else:
            session['user'] = {'username': user.nom_usuario, 'role': user.rol}  # Almacenamos el ID del usuario en la sesión
            if user.rol == 1:
                # Redireccionar a la vista de administrador
                return redirect(url_for('home.cerrar'))
            elif user.rol == 2:
                # Redireccionar a la vista de empleado
                return redirect(url_for('ventas.sale'))
            else:
                flash('No tienes un rol válido', 'error')
    return render_template('login/login.html', form=form)

@login_views.route('/logout/')
def logout():
    print('Cerrando session')
    session.clear()
    print(session)  # Remueve el ID del usuario de la sesión
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('home.cat'))  # Redirige al formulario de inicio de sesión