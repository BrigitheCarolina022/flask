from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import InputRequired

       
class NewClientesForm(FlaskForm) :
    
        nombre = StringField("Ingrese su nombre :",
                         validators = [
                             InputRequired(message='Por favor ingrese su nombre')])
        password = StringField("Ingrese su password :",
                         validators = [
                             InputRequired(message='Por favor ingrese su password')])
    
        email = StringField("Ingrese su email :",
                         validators = [
                             InputRequired(message='Por favor ingrese su email')])
        submit = SubmitField("Guardar")
    
class EditClientesFrom(FlaskForm):
    submit = SubmitField("Actualizar")
