"""agendamiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from citas.views import Viendocitas, Viendoeps, Viendoperfil, Viendopaciente, Viendomedico, Insertarcita, Editarcita, Eliminarcita, Editareps, Insertareps, Eliminareps, Insertarmedico, Editarmedico, Eliminarmedico, Editarpaciente, Eliminarpaciente, Insertarpaciente, Editarperfil, Eliminarperfil, Insertarperfil
from django.conf.urls.static import static
from agendamiento import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path ('vercita/', Viendocitas.as_view()),
    path('insertarcita/', Insertarcita.as_view()),
    path('editarcita/<int:pk>/', Editarcita.as_view()),
    path('elicita/<int:pk>/', Eliminarcita.as_view()),
    path ('vereps/', Viendoeps.as_view()),
    path('insertareps/', Insertareps.as_view()),
    path('editareps/<int:pk>/', Editareps.as_view()),
    path('elieps/<int:pk>/', Eliminareps.as_view()),
    path ('verperfil/',Viendoperfil.as_view()),
    path('insertarperfil/', Insertarperfil.as_view()),
    path('editarperfil/<int:pk>/', Editarperfil.as_view()),
    path('eliperfil/<int:pk>/', Eliminarperfil.as_view()),
    path ('verpaciente/', Viendopaciente.as_view()),
    path('insertarpaciente/', Insertarpaciente.as_view()),
    path('editarpaciente/<int:pk>/', Editarpaciente.as_view()),
    path('elipaciente/<int:pk>/', Eliminarpaciente.as_view()),
    path ('vermedico/', Viendomedico.as_view()),
    path('insertarmedico/', Insertarmedico.as_view()),
    path('editarmedico/<int:pk>/', Editarmedico.as_view()),
    path('elimedico/<int:pk>/', Eliminarmedico.as_view()),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view()),


]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


