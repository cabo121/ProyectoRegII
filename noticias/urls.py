from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from .views import password_reset_request,eliminarCorona,eliminarDep,eliminarNac,agregarCorona,agregarDep,agregarNac,modificarCorona,modificarNac,modificarDep,AcercaPageView,DeportesPageView,NacionalesPageView,CoronaPageView,HomePageView,RegistroPageView,registro_usuario,changePassword

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('registration/registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registration/registrar', registro_usuario, name='registrar'),
	path('change_password/', changePassword, name = 'change_password' ),
	path("password_reset", password_reset_request, name="password_reset"),
	path('acerca',AcercaPageView.as_view(),name = 'acerca'),
	path('deportes',DeportesPageView.as_view(),name = 'deportes'),
	path('corona',CoronaPageView.as_view(),name = 'corona'),
	path('nacionales',NacionalesPageView.as_view(),name = 'nacionales'),
	path('modificarCorona/<id>/',modificarCorona, name = 'modificarCorona'),
	path('eliminarCorona/<id>/',eliminarCorona, name = 'eliminarCorona'),
	path('agregarCorona/',agregarCorona, name = 'agregarCorona'),
	path('modificarDep/<id>/',modificarDep, name = 'modificarDep'),
	path('eliminarDep/<id>/',eliminarDep, name = 'eliminarDep'),
	path('agregarDep/',agregarDep, name = 'agregarDep'),
	path('modificarNac/<id>/',modificarNac, name = 'modificarNac'),
	path('eliminarNac/<id>/',eliminarNac, name = 'eliminarNac'),
	path('agregarNac/',agregarNac, name = 'agregarNac'),
]