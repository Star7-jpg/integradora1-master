from flask import Blueprint, render_template, redirect, url_for, flash, abort


login_views = Blueprint ('login',__name__)

@login_views.route("/login")
def login():
    return render_template('login/login.html')

@login_views.route("/home")
def adm_home():
    return render_template('home/menu_adm.html')