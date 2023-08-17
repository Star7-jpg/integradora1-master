<<<<<<< HEAD
from flask import Blueprint, session,render_template, redirect, url_for, request, flash, session, abort
=======
from flask import Blueprint, session,render_template, redirect, url_for, request, flash, abort, session
>>>>>>> c48ae21c87754321f63b1dad2a4976c86d1d5810
from models.sale import Sale
from models.product import Product
from models.user import User
from forms.sale_forms import CreateSaleForm

sale_views = Blueprint ('ventas', __name__)

@sale_views.route('/sale/')
def sale():
<<<<<<< HEAD
   if session.get('user') and session.get('user')['role']==2:
        sale = Sale.get_all()
        return render_template('sale/sale.html',
                            sale=sale)
   else:
      abort(403)
      
=======
    if session.get('user')['rol'] == 2:
        sale = Sale.get_all()
        return render_template('sale/sale.html',
                           sale=sale)
    else:
        abort(403)


>>>>>>> c48ae21c87754321f63b1dad2a4976c86d1d5810
@sale_views.route('/sale/create/', methods=('GET','POST'))
def create_sal():
   if session.get('user') and session.get('user')['role']==2:
        form = CreateSaleForm()

        product = Product.get_all2()
        pros = [(-1, '')]
        for pro in product:
            pros.append((pro.id_producto, pro.nombre))
        form.id_producto.choices = pros

        user = User.get_all()
        uses = [(-1, '')]
        for use in user:
            uses.append((use.id_usuario, use.nombre))
        form.id_usuario.choices = uses

        if form.validate_on_submit():
            fecha = form.fecha.data
            total = form.total.data
            id_producto = form.id_producto.data
            id_usuario = form.id_usuario.data
            unidades_vendidas = form.unidades_vendidas.data
            sal = Sale( fecha=fecha, 
                        total=total, 
                        id_producto=id_producto, 
                        id_usuario=id_usuario, 
                        unidades_vendidas=unidades_vendidas)
            sal.save()
            return redirect(url_for('ventas.sale'))
        return render_template('sale/create_sal.html', form=form)
   else:
       abort(403)
    
    