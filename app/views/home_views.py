from flask import Blueprint, render_template, session, abort
from flask_session import Session

home_views = Blueprint ('home',__name__)

@home_views.route("/hola/")
def cerrar():
<<<<<<< HEAD
    if session.get('user') and session.get('user')['role']==1:
        return render_template('home/menu_adm.html')
    else: 
        abort(403)


@home_views.route("/")
def cat():
    return render_template('home/cierreSesion.html')


@home_views.route("/terminos")
def term():
    return render_template('reports/terminos.html/')
=======
    session.pop('id_usuario', None)
    return render_template('home/cierreSesion.html')
>>>>>>> c48ae21c87754321f63b1dad2a4976c86d1d5810
