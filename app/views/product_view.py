from flask import Blueprint, render_template, redirect, url_for,request, flash

product_views =Blueprint ('product',__name__)

@product_views.route("/productos")
def productos():
    return render_template('products/products.html')

@product_views.route("/crear_productos")
def c_produ():
    return render_template('products/create_prod.html')