from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import deportes, nacionales, corona
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#--------------------------------------------------------------------------
# FORMULARIOS DEL USUARIO PERSONALIZADO
#--------------------------------------------------------------------------

class CustomUserForm (UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

#--------------------------------------------------------------------------
# FORMULARIOS DE CADA MODELO DE LA BASE DE DATOS
#--------------------------------------------------------------------------

class NacForm (forms.ModelForm):
	
	class Meta:
		model = nacionales
		fields = '__all__'

class DepForm (forms.ModelForm):
	
	class Meta:
		model = deportes
		fields = '__all__'

class CoroForm (forms.ModelForm):
	
	class Meta:
		model = corona
		fields = '__all__'
