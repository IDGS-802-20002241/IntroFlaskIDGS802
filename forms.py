from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField,RadioField
from wtforms import EmailField

class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apaterno=StringField("apaterno")
    materias=SelectField(choices=[('Español','esp'),('Matematicas','mat'), ('Ingles','ING') ])
    radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])