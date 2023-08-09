from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateSaleForm(FlaskForm):

    pros=[]

    fecha = StringField('Fecha', 
                           validators=[DataRequired()])

    total = StringField('Total', 
                           validators=[DataRequired()])

    id_producto = SelectField('Producto', choices=pros, coerce=int, validate_choice=False, validators=[DataRequired()])

    id_usuario = StringField('Usuario', 
                           validators=[DataRequired()])
    
    unidades_vendidas = StringField('Unidades Vendidas',
                            validators=[DataRequired()])
    
    
    submit = SubmitField('Guardar')

class UpdateSaleForm(FlaskForm):
    fecha = StringField('Fecha', 
                           validators=[DataRequired()])

    total = StringField('Total', 
                           validators=[DataRequired()])

    id_producto = StringField('Producto', 
                           validators=[DataRequired()])

    id_usuario = StringField('Usuario', 
                           validators=[DataRequired()])
    
    unidades_vendidas = StringField('Unidades Vendidas',
                            validators=[DataRequired()])
    
     
    submit = SubmitField('Guardar')