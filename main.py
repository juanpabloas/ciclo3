import yagmail as yagmail
from flask import Flask,render_template,request,redirect,url_for,flash
import utils
import os
from markupsafe import escape #inyeccion de codigo
from form import formInicio
from form import formRegistro
import sqlite3


app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/',methods=['GET','POST'])
def iniciarsesion():
    form = formInicio()
    if (form.validate_on_submit()):
        flash("inicio de sesión solicitado por el usuario{} ".format(form.txtNombre.data))
        return redirect(url_for("gracias"))
    if request.method=='POST'and 'signup' in request.form:    
        return redirect(url_for("registro"))
    elif request.method=='POST'and 'forget-password' in request.form:    
        return redirect(url_for("recuperarcontraseña"))
    return render_template("iniciar_sesion.html", form=form)



@app.route('/principal')
def principal():
    return render_template("principal.html")


@app.route('/registro',methods=['GET','POST'])
def registro():
    form=formRegistro()   
    try: 
       if request.method=='POST':
           nombres = escape(request.form["nombres"])
           apellidos = escape(request.form["apellidos"]) 
           correo = escape(request.form["correo"])  
           password = escape(request.form["password"])  
           error = None
           if not utils.isUsernameValid(nombres):
               error = "El nombre debe ser alfanumerico"
               flash(error)
               return render_template("datosRegistro.html")

           if not utils.isUsernameValid(apellidos):
               error = "Los apellidos deben ser alfanumerico"
               flash(error)
               return render_template("datosRegistro.html")

           if not utils.isEmailValid(correo):
               error = "El correo es inválido" 
               flash(error)
               return render_template("datosRegistro.html") 

           if not utils.isPasswordValid(password):
               error = "La contraseña es inválida"
               flash(error)
               return render_template("datosRegistro.html")
            
           yag = yagmail.SMTP("pruebatk.8912@gmail.com","prueba123")
           yag.send(to=correo,subject="Activa tu cuenta",contents="Bienvenido xxx")
           flash("Revisa tu correo para activar tu cuenta")
           return render_template("iniciarsesion.html")
       return render_template("datosRegistro.html", form=form) 
    except:
       return render_template("datosRegistro.html", form=form)  

@app.route('/actualizar')
def actualizar():
    return render_template("actualizar.html")

@app.route('/comentar')
def comentar():
    return render_template("comentar.html")


@app.route('/gracias')
def gracias():
    return render_template("gracias.html")     
    
@app.route('/recuperarcontraseña')
def recuperarcontraseña():
    return render_template("recuperarContrasena.html")

@app.route('/crear')
def crear():
    return render_template("crear.html")

@app.route("/usuario/guardar", methods=['GET','POST'])
def estudiante_save():
    form = formRegistro()
    if request.method == "POST":
        nombres = form.nombres.data
        apellidos = form.apellidos.data
        correo = form.correo.data
        #password = form.password.data       
        confirmar_password = form.confirmar_password.data       
        estado = form.estado.data       
        try:
            with sqlite3.connect('blogs.db') as con: 
                cur = con.cursor()
                cur.execute("INSERT INTO Usuario(nombres,apellidos,correo,contraseña,estado)VALUES(?,?,?,?,?)",(nombres,apellidos,correo,confirmar_password,estado))
                con.commit()
                return "Guardado Satisfactoriamente" 
        except: 
            con.rollback()
    return "No se pudo guardar"

if __name__ == "__main__":
    app.run(debug=True)        