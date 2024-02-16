from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField,RadioField,IntegerField
from wtforms import EmailField
from wtforms import validators

""" class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apaterno=StringField("apaterno")
    materias=SelectField(choices=[('Español','esp'),('Matematicas','mat'), ('Ingles','ING') ])
    radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')]) """
    
class UserForm(Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message='Ingrese un nombre válido')
    ])
    email = EmailField("correo", [
        validators.Email(message='Ingrese un correo válido')
    ])
    apaterno = StringField("apaterno")
    edad = IntegerField("edad", [
        validators.NumberRange(min=1, max=20, message='Ingrese un valor válido, debe estar entre 1 y 20')
    ])

    """ materias=SelectField(choices=[('Español','esp'),('Matematicas','mat'), ('Ingles','ING') ])
    radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')]) """