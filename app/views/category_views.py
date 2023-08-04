from flask import Blueprint, render_template, redirect ,url_for,request,flash
from models.categories import Category

from forms.category_forms import CreateCategoryForm, UpdateCategoryForm
category_view =Blueprint('cat',__name__)

@category_view.route("/categorias/")
def catp():
    category=Category.get_all()
    return render_template("/categories/categories.html",
                            categories=category)

@category_view.route("/crear", methods=('GET','POST'))
def catn():
    form = CreateCategoryForm()
    if form.validate_on_submit():
        nombre= form.nombre.data
        cat = Category(nombre)
        cat.save()
        return redirect(url_for('cat.catp'))
    return render_template("/categories/create_cat.html", form=form)

@category_view.route("/categorias/<int:id_categoria>/editar", methods=('GET','POST'))
def cate(id_categoria):
    form= UpdateCategoryForm()
    cate=Category.get(id_categoria)
    if form.validate_on_submit():
        cate.nombre=form.nombre.data
        cate.save()
        return redirect(url_for('cat.catp'))
    form.nombre.data =cate.nombre
    return render_template("/categories/edit_cat.html", form=form)

@category_view.route('/categories/<int:id_categoria>/delete/', methods =('POST',))
def delete_cat(id_categoria):
    #Obtener Cat desde id
    cat = Category.get(id_categoria)
    cat.delete()
    #Enviar datos a form
    return redirect(url_for('cat.catp'))
