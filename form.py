from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class formInicio(FlaskForm):
    txtNombre = StringField("txtNombre",validators=[DataRequired(message = "No dejar vacio")])
    txtPw1 = PasswordField("txtPw1",validators=[DataRequired(message = "Contraseña requerida")])
    recordar = BooleanField("Recordar usuario")
    enviar = SubmitField("Iniciar sesion")
    olvidar = SubmitField("Olvidó su contraseña?")
    registrar = SubmitField("Registrarse")
    