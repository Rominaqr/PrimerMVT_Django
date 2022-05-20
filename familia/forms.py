#La sintaxis de declaración para un formulario es muy similar a la de declarar un modelo, 
# y comparte los mismos tipos de campo (y algunos parámetros similares). Esto tiene sentido porque en ambos
#  casos debemos asegurarnos de que cada campo maneja los tipos correctos de datos, está restringido a datos válidos
#  y tiene una descripción para la visualización / documentación. 
# Para crear un formulario (Form) es necesario importar la libreria forms, derivada de la clase Form, 
# y tambien declarar los campos del formulario. A continuación se muestra una clase de formulario muy básica 
# para nuestro formulario de renovación de libros de la biblioteca:
from django import forms
from django.forms.widgets import NumberInput

listaGenero=[('Femenino', 'Femenino'),
    ('Masculino', 'Masculino')]
    
listaRelation=[('Madre', 'Madre'),
    ('Padre', 'Padre'),
    ('Hermana', 'Hermana'),
    ('Sobrino', 'Sobrino'),
    ('Primo', 'Primo'),
    ('Abuelo', 'Abuelo')]

class personaForm(forms.Form):
    firstname = forms.CharField(label='Nombre', max_length=100)
    lastname = forms.CharField(label='Apellido', max_length=100)
    gender= forms.CharField(label='Genero', widget=forms.Select(choices=listaGenero))
    age= forms.IntegerField(label='Edad')
    #birtdate=forms.DateField(label='Fecha Nacimiento', help_text="Ingrese fecha de nacimiento DD/MM/YYYY")
    birthdate=forms.DateField(label='Fecha Nacimiento', widget=NumberInput(attrs={'type': 'date'}))
    relation= forms.CharField(label='Parentesco', widget=forms.Select(choices=listaRelation))
    email = forms.EmailField(max_length=100, label='Email')

