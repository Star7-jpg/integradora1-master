from flask import Blueprint, render_template, redirect, url_for,request, flash
from models.product import Product

from forms.product_forms import CreateProductForm,UpdateProductForm
product_views =Blueprint ('product',__name__)

@product_views.route("/productos")
def productos():
    product = Product.get_all()
    return render_template('/product/product.html',
                           product=product)

@product_views.route("/crear_productos", methods=('GET','POST'))
def c_produ():
    form= CreateProductForm()
    if form.validate_on_submit():
        nombre= form.nombre.data
        precio=form.precio.data
        descripcion=form.descripcion.data
        id_marca=form.id_marca.data
        id_categoria= form.id_categoria.data
        prod= Product(nombre, precio,descripcion,id_marca,id_categoria)
        prod.save()
        return redirect(url_for('product.productos'))
    return render_template('product/create_pro.html', form=form)



@product_views.route("/productos/<int:id_producto>/actualizar", methods=('GET','POST'))
def updateprod(id_producto):
    form=UpdateProductForm()
    prod=Product.get(id_producto)
    if form.validate_on_submit():
        prod.nombre=form.nombre.data
        prod.precio=form.precio.data
        prod.descripcion=form.descripcion.data
        prod.id_marca=form.id_marca.data
        prod.id_categoria=form.id_categoria.data
        prod.save()
        return redirect(url_for('product.productos'))
    form.nombre.data=prod.nombre
    form.precio.data=prod.precio
    form.descripcion.data=prod.descripcion
    form.id_marca.data=prod.id_marca
    form.id_categoria.data= prod.id_categoria
    return render_template('/product/update_prod.html',form=form)

@product_views.route("/productos/<int:id_producto>/eliminar", methods=('POST',))
def delprod(id_producto):

    prod= Product.get(id_producto)
    prod.delete()

    return redirect(url_for('product.productos'))