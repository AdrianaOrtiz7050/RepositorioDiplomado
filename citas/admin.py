from django.contrib import admin #por defecto me trae laslibrerias del administrador

from citas.models import Agendamiento, User, Paciente, Medico, Eps, Profile #llamar las tablas de models.py

# Register your models here.


@admin.register(Agendamiento)
class Adminagendamiento(admin.ModelAdmin):
   list_display = ('id','tipocita', 'fecha', 'nombre_medico', 'nombre_paciente',)
   list_filter = ('tipocita',)
   def nombre_medico(self, medicon):
       return "%s %s" % (medicon.medico.user.first_name , medicon.medico.user.last_name)
   def nombre_paciente(self, pacienten):
       return "%s %s" % (pacienten.paciente.user.first_name , pacienten.paciente.user.last_name)

@admin.register(Paciente)
class Adminpaciente(admin.ModelAdmin):
    list_display = ('id','eps','user',)


@admin.register(Medico)
class Adminmedico(admin.ModelAdmin):
    list_display = ('id','especialidad','user',)


@admin.register(Eps)
class Admineps(admin.ModelAdmin):
    list_display = ('id', 'eps',)

@admin.register(Profile)
class Adminprofile(admin.ModelAdmin):
    list_display = ('id', 'genero', 'documento', 'telefono', 'nacimiento', 'user',)




