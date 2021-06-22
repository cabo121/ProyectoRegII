from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import deportes, nacionales, corona
from .forms import DepForm, NacForm, CoroForm , CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

#--------------------------------------------------------------------------
# VISTAS DE CADA SECCION DE LA PAGINA WEB
#--------------------------------------------------------------------------

class HomePageView(ListView):
	model = deportes
	template_name = 'home.html'
	context_object_name = 'docs_list'

class DeportesPageView(ListView):
	model = deportes
	template_name = 'deportes.html'
	context_object_name = 'docs_list'

class NacionalesPageView(ListView):
	model = nacionales
	template_name = 'nacionales.html'
	context_object_name = 'docs_list'

class CoronaPageView(ListView):
	model = corona
	template_name = 'corona.html'
	context_object_name = 'docs_list'

class AcercaPageView(ListView):
	model = deportes
	template_name = 'acercade.html'
	context_object_name = 'docs_list'

#--------------------------------------------------------------------------
# VISTAS DEL MANEJO DE LOS USUARIOS (REGISTRAR, CAMBIO DE CONTRASENA)
#--------------------------------------------------------------------------

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registration/registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = deportes
	template_name = 'registration/registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUserForm()
	}

	if request.method == 'POST':
		formulario = CustomUserForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='registro_success')
		else:
			data['form'] = formulario
			
	return render(request, 'registration/registrar.html', data)	

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})


#--------------------------------------------------------------------------
# VISTAS PARA LA MANIPULACION DE LOS MODELOS DE LA BASE DE DATOS
#--------------------------------------------------------------------------
# MODELO DEPORTES

@permission_required('noticias.add_deportes')
def agregarDep (request):
	
	if request.method == "GET":
		form = DepForm()
	else:
		form = DepForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Anadido con exito")
			return redirect('deportes')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarDep.html', {"form": form})


@permission_required('noticias.change_deportes')
def modificarDep (request, id):

	Dep = get_object_or_404(deportes, id=id)

	data = {
		'form': DepForm(instance=Dep)
	}

	if request.method == "GET":
		form = DepForm()
	else:
		form = DepForm(request.POST,request.FILES, instance=Dep)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('deportes')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('noticias.delete_deportes')
def eliminarDep (request, id):
	Dep = get_object_or_404(deportes, id=id)
	Dep.delete()

	return redirect(to = "deportes")


#----------------------------------------------------------------------
# MODELO NACIONAL

@permission_required('noticias.add_nacionales')
def agregarNac (request):
	
	if request.method == "GET":
		form = NacForm()
	else:
		form = NacForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Anadido con exito")
			return redirect('nacionales')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarNac.html', {"form": form})


@permission_required('noticias.change_nacionales')
def modificarNac (request, id):

	Nac = get_object_or_404(nacionales, id=id)

	data = {
		'form': NacForm(instance=Nac)
	}

	if request.method == "GET":
		form = NacForm()
	else:
		form = NacForm(request.POST,request.FILES, instance=Nac)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('nacionales')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('noticias.delete_nacionales')
def eliminarNac (request, id):
	Nac = get_object_or_404(nacionales, id=id)
	Nac.delete()

	return redirect(to = "nacionales")
	

#----------------------------------------------------------------------
# MODELO CORONAVIRUS

@permission_required('noticias.add_corona')
def agregarCorona (request):
	
	if request.method == "GET":
		form = CoroForm()
	else:
		form = CoroForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Anadido con exito")
			return redirect('corona')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarCorona.html', {"form": form})


@permission_required('noticias.change_corona')
def modificarCorona (request, id):

	Coro = get_object_or_404(corona, id=id)

	data = {
		'form': CoroForm(instance=Coro)
	}

	if request.method == "GET":
		form = CoroForm()
	else:
		form = CoroForm(request.POST,request.FILES, instance=Coro)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('corona')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('noticias.delete_corona')
def eliminarCorona (request, id):
	Coro = get_object_or_404(corona, id=id)
	Coro.delete()

	return redirect(to = "corona")
	

#----------------------------------------------------------------------
