from flask import Blueprint, render_template, session
from flask_session import Session

home_views = Blueprint ('home',__name__)

@home_views.route("/")
@home_views.route("/hola/")
def cerrar():
    session.pop('id_usuario', None)
    return render_template('home/cierreSesion.html')