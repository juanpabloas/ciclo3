import yagmail as yagmail
from flask import Flask,render_template,request,redirect,url_for,flash
import utils
import os
app=Flask(__name__)
app.secret_key=os.urandom(24)


@app.route('/')
def principal():
    return render_template("principal.html")


@app.route('/registro',methods=['GET','POST'])
def registro():
    try: 
        if request.method=='POST':
            user_name = request.form["txtNombre"]
            email = request.form["txtEma"] 
            clave = request.form["txtPw1"]  
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
    return render_template("IniciarSesion.html")
     
    

@app.route('/recuperarcontraseña')
def recuperarcontraseña():
    return render_template("recuperarContraseña.html")

@app.route('/crear')
def crear():
    return render_template("crear.html")



if __name__ == "__main__":
    app.run(debug=True)        