from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class formInicio(FlaskForm):
    usuari = StringField("usuario",validators=[DataRequired(message = "No dejar vacio")], render_kw={"placeholder":"Correo"})
    clave = PasswordField("clave",validators=[DataRequired(message = "Contraseña requerida")], render_kw={"placeholder":"Contraseña"})
    recordar = BooleanField("Recordar usuario")
    enviar = SubmitField("Iniciar sesion")
    olvidar = SubmitField("Olvidó su contraseña?")
    registrar = SubmitField("Registrarse")


class formRegistro(FlaskForm):
    nombres = StringField("Nombre",validators = [DataRequired(message="No dejar vacío, completar")], render_kw={"placeholder":"Nombres"})
    apellidos = StringField("Apellidos",validators = [DataRequired(message="No dejar vacío, completar")], render_kw={"placeholder":"Apellidos"})
    correo = StringField("Correo",validators = [DataRequired(message="No dejar vacío, completar")], render_kw={"placeholder":"Correo"})
    password = PasswordField("Password",validators = [DataRequired(message="No dejar vacío, completar")], render_kw={"placeholder":"Contraseña"})
    confirmar_password = PasswordField("Confirmar Password",validators = [DataRequired(message="No dejar vacío, completar")], render_kw={"placeholder":"Confirmar la contraseña"})
    estado = BooleanField("Estoy de acuerdo con los términos y condiciones")
    enviar = SubmitField("Enviar", render_kw={"onmouseover":"guardar_usuario()"})
    
    