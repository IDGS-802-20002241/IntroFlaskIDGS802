from flask import Flask, request, render_template,Response
from flask_wtf.csrf import CSRFProtect
import forms 
from flask import flash
from flask import g
app=Flask(__name__)
app.secret_key='esta es la clave secreta'
'''     
Decoradores o rutas
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_reques():
    g.prueba='hola'
    print('Antes de ruta')
    
@app.after_request
def after_request(response):
    print('Despues de la ruta 3')
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    print('dentro 2')
    valor=g.prueba
    print('el dato es: {}'.format(valor))
    alumn_form=forms.UserForm(request.form)
    if request.method == 'POST' and alumn_form.validate():
        nom=alumn_form.nombre.data    
        email=alumn_form.email.data    
        apaterno=alumn_form.apaterno.data   
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom)) 
        print("email: {}".format(email)) 
        print("Apellido paterno: {}".format(apaterno)) 
    return render_template("alumnos.html", form =alumn_form )


@app.route("/maestros")
def maestros():
    return render_template("maestros.html")



def hola():
    return "<p>Hola mundo<p>"



@app.route("/hola")

def func():
    return "<p>Saludo desde hola<p>"

@app.route("/saludo")
def func1():
    return "<p>Saludo desde saludo con alguna de los decoradores<p>"


@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<p><p>" +nom



@app.route("/numero/<int:n1>")
def numero(n1):
    return "<p>El valor es {}<p>".format(n1)


@app.route("/varios/<string:nom>/<int:id>")
def cadena(nom,id):
    return "ID {} NOMBRE {}".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
        
    
    return "La suma de {} + {} = {}".format(n1,n2,n1+n2) 



@app.route("/multiplica",methods=["GET","POST"])
def mult():
    if request.method== "POST":
        num1 =request.form.get("n1")
        num2 =request.form.get("n2")
        
        return "<h1>el resultado es: {} </h1>".format(str(int(num1)*int(num2)))
    else:
       
        return '''
            <form action="/multiplica" method="POST">
            <label>N1: </label>
            <input type="text" name="n1">
            <label>N2: </label>
            <input type="text" name="n2">
            <input type="submit">
            </form>
                '''

@app.route("/formulario1",methods=["GET","POST"])
def calculo():
    return render_template("formulario1.html")
   
@app.route("/resultado",methods=["GET","POST"])
def mult1():
    if request.method== "POST":
        num1 =request.form.get("n1")
        num2 =request.form.get("n2")
        
        return "<h1>El resultado es: {} </h1>".format(str(int(num1)*int(num2)))
    
@app.route("/practica1")
def practica():
    return render_template("layout2.html")

if __name__ == "__main__":
    app.run(debug=True)   
