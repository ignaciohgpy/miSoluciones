#-*- coding: utf-8 -*-
from django import forms
from Soluciones.models import soluciones,paquetes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FormularioPaquetes(forms.ModelForm):
    class Meta:
        model=paquetes
        fields =("paqueteCod",
                 "paqueteCant","paquetePrecio","paqueteDias","paqueteDescr","paquetePerfil")


class Formulario(forms.ModelForm):
    class Meta:
        model = soluciones
        fields ='__all__'

class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')