from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort
from models.user import User
from forms.user_forms import CreateUserForm, UpdateUserForm

user_views = Blueprint ('usuario', __name__)

@user_views.route('/user/')
def user():
<<<<<<< HEAD
    if session.get('user') and session.get('user')['role']==1:
        user = User.get_all()
        return render_template('user/user.html',
                            user=user)
    else: 
=======
    if session.get('user')['rol'] == 1:
        user = User.get_all()
        return render_template('user/user.html',
                           user=user)
    else:
>>>>>>> c48ae21c87754321f63b1dad2a4976c86d1d5810
         abort(403)

@user_views.route('/user/create/', methods=('GET','POST'))
def create_use():
    if session.get('user') and session.get('user')['role']==1:
        form = CreateUserForm()
        if form.validate_on_submit():
                nombre = form.nombre.data
                ape_paterno = form.ape_paterno.data
                ape_materno = form.ape_materno.data
                nom_usuario = form.nom_usuario.data
                contrasenia = form.contrasenia.data
                rol = form.rol.data
                use = User(nombre, ape_paterno, ape_materno, nom_usuario, contrasenia, rol)
                use.save()
                return redirect(url_for('usuario.user'))
        
        return render_template('user/create_use.html', form=form)
    else:
         abort(403)

@user_views.route('/user/<int:id_usuario>/update/', methods=('GET', 'POST'))
def update_use(id_usuario):
    if session.get('user') and session.get('user')['role']==1:
        form = UpdateUserForm() #Obtener Cat desde id
        use = User.__get__(id_usuario)
        if form.validate_on_submit():
            use.nombre = form.nombre.data
            use.ape_paterno = form.ape_paterno.data
            use.ape_materno = form.ape_materno.data
            use.nom_usuario = form.nom_usuario.data
            use.contrasenia = form.contrasenia.data
            use.rol = form.rol.data
            use.save()
            return redirect(url_for('usuario.user'))
        form.nombre.data = use.nombre
        form.ape_paterno.data = use.ape_paterno
        form.ape_materno.data = use.ape_materno
        form.nom_usuario.data = use.nom_usuario
        form.contrasenia.data = use.contrasenia
        form.rol.data = use.rol
        return render_template('user/create_use.html', form=form) #enviar datos a form
    else:
        abort(403)

@user_views.route('/user/<int:id_usuario>/delete/', methods=('POST', 'GET'))
def delete_use(id_usuario):
    #Obtener Cat desde id
    use = User.__get__(id_usuario)
    use.delete()
    #enviar datos a form
    return redirect(url_for('usuario.user'))