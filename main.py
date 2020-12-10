import yagmail as yagmail
from flask import Flask,render_template,request,redirect,url_for,flash
import utils
import os
from markupsafe import escape #inyeccion de codigo
from form import formInicio

app=Flask(__name__)
app.secret_key=os.urandom(24)


@app.route('/')
def principal():
    return render_template("principal.html")


@app.route('/registro',methods=['GET','POST'])
def registro():
    try: 
        if request.method=='POST':
            user_name = escape(request.form["txtNombre"])
            email = escape(request.form["txtEma"]) 
            clave = escape(request.form["txtPw1"])  
            error = None

            if not utils.isUsernameValid(user_name):
                error = "El nombre debe ser alfanumerico"
                flash(error)
                return render_template("datosRegistro.html")
            
            if not utils.isPasswordValid(clave):
                error = "La contraseña es inválida"
                flash(error)
                return render_template("datosRegistro.html")

            if not utils.isEmailValid(email):
                print("4")
                error = "El correo es inválido" 
                flash(error)
                return render_template("datosRegistro.html")     

            yag = yagmail.SMTP("pruebatk.8912@gmail.com","prueba123")
            yag.send(to=email,subject="Activa tu cuenta",contents="Bienvenido xxx")
            flash("Revisa tu correo para activar tu cuenta")
            return render_template("iniciarsesion.html")
        return render_template("datosRegistro.html")
    except:
        return render_template("datosRegistro.html")   

@app.route('/actualizar')
def actualizar():
    return render_template("actualizar.html")

@app.route('/comentar')
def comentar():
    return render_template("comentar.html")

@app.route('/Iniciarsesion',methods=['GET','POST'])
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

@app.route('/gracias')
def gracias():
    return render_template("gracias.html")     
    
@app.route('/recuperarcontraseña')
def recuperarcontraseña():
    return render_template("recuperarContrasena.html")

@app.route('/crear')
def crear():
    return render_template("crear.html")

if __name__ == "__main__":
    app.run(debug=True)        