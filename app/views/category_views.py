from flask import Blueprint, render_template, redirect ,url_for,request,flash, session, abort
from models.categories import Category
import math

from forms.category_forms import CreateCategoryForm, UpdateCategoryForm
category_view =Blueprint('cat',__name__)

@category_view.route("/categorias/")
@category_view.route("/categorias/<int:page>/")
def catp(page=1):
    if session.get('user') and session.get('user')['role']==1:
        limit=10

        category=Category.get_all(limit=limit, page=page)
        total_cat = Category.count()
        pages = math.ceil(total_cat / limit)
        
        return render_template("/categories/categories.html",
                                categories=category, page=page, pages=pages)
    else:
        abort(403)

@category_view.route("/categorias/crear", methods=('GET','POST'))
def catn():
    if session.get('user') and session.get('user')['role']==1:
        form = CreateCategoryForm()
        if form.validate_on_submit():
            nombre= form.nombre.data
            cat = Category(nombre)
            cat.save()
            return redirect(url_for('cat.catp'))
        return render_template("/categories/create_cat.html", form=form)
    else:
        abort(403)

@category_view.route("/categorias/<int:id_categoria>/editar", methods=('GET','POST'))
def cate(id_categoria):
    if session.get('user') and session.get('user')['role']==1:
        form= UpdateCategoryForm()
        cate=Category.get(id_categoria)
        if form.validate_on_submit():
            cate.nombre=form.nombre.data
            cate.save()
            return redirect(url_for('cat.catp'))
        form.nombre.data =cate.nombre
        return render_template("/categories/edit_cat.html", form=form)
    else:
        abort(403)

@category_view.route('/categories/<int:id_categoria>/delete/', methods =('POST',))
def delete_cat(id_categoria):
    
    #Obtener Cat desde id
    cat = Category.get(id_categoria)
    cat.delete()
    #Enviar datos a form
    return redirect(url_for('cat.catp'))
