from flask import Blueprint, render_template

category_view =Blueprint('cat',__name__)
@category_view.route("/categorias")
def catp():
    return render_template("/category/categorias.html")

@category_view.route("/crear")
def catn():
    return render_template("/category/creat_cat.html")

@category_view.route("/crear")
def cate():
    return render_template("/category/edit_cat.html")
