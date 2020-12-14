import yagmail as yagmail
from flask import Flask,render_template,request,redirect,url_for,flash, session
import utils
import os
from markupsafe import escape #inyeccion de codigo
from form import formInicio
from form import formRegistro
import sqlite3
from markupsafe import escape


app=Flask(__name__)
app.secret_key=os.urandom(24)


@app.route('/',methods=['GET','POST'])
def iniciarsesion1():
    form = formInicio() 
    
    if request.method=='POST' and 'iniciar_sesion' in request.form:                      
        usuari = escape(request.form["usuario"])
        clav = escape(request.form["clave"])
        with sqlite3.connect('blogs.db') as con: 
            cur = con.cursor()           
            cur.execute("SELECT * FROM Usuario WHERE correo = ? AND contraseña = ?",(usuari,clav))
            if cur.fetchone():
                session["usuario"] = usuari 
                return render_template("principal.html",form=form)
        return "Usuario no permitido"
        
    if request.method =='POST' and 'signup' in request.form:    
        return redirect(url_for("registro"))
    elif request.method =='POST'and 'forget-password' in request.form:    
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
        #    password = escape(request.form["password"])  
           confirmar_password = escape(request.form["confirmar_password"])  
           estado = escape(request.form["estado"])  
        #    error = None
        #    if not utils.isUsernameValid(nombres):
        #        error = "El nombre debe ser alfanumerico"
        #        flash(error)
        #        return render_template("datosRegistro.html")
        #    if not utils.isUsernameValid(apellidos):
        #        error = "Los apellidos deben ser alfanumerico"
        #        flash(error)
        #        return render_template("datosRegistro.html")
        #    if not utils.isEmailValid(correo):
        #        error = "El correo es inválido" 
        #        flash(error)
        #        return render_template("datosRegistro.html") 
        #    if not utils.isPasswordValid(password):
        #        error = "La contraseña es inválida"
        #        flash(error)
        #        return render_template("datosRegistro.html")
        #    if not utils.isPasswordValid(confirmar_password):
        #        error = "La contraseña es inválida"
        #        flash(error)
        #        return render_template("datosRegistro.html")
            
           try:
               with sqlite3.connect('blogs.db') as con: 
                   cur = con.cursor()
                   cur.execute("INSERT INTO Usuario(nombres,apellidos,correo,contraseña,estado)VALUES(?,?,?,?,?)",(nombres,apellidos,correo,confirmar_password,estado))
                   con.commit()
                   return "Guardado Satisfactoriamente" 

           except:
               con.rollback()
            
        #    yag = yagmail.SMTP("pruebatk.8912@gmail.com","prueba123")
        #    yag.send(to=correo,subject="Activa tu cuenta",contents="Bienvenido xxx")
        #    flash("Revisa tu correo para activar tu cuenta")
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

@app.route("/logout")
def logout():
    if "usuari" in session:
        session.pop("usuari", None)
        return render_template("logout.html")
    else:
        return "Ya se cerró la sesión"

if __name__ == "__main__":
    app.run(debug=True)        