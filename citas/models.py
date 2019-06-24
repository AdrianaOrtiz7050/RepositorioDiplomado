from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Profile (models.Model):

    genero=((1, "M"),
            (2, "F"),
            (3, "O"),)

    documento=models.CharField(max_length=11)
    telefono=models.CharField(max_length=10)
    nacimiento=models.DateField()
    genero=models.SmallIntegerField(choices=genero)

    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='profile'

class Eps (models.Model):

    eps=models.CharField(max_length=50)

    class Meta:
        db_table='eps'

    def __str__(self):
        return self.eps



class Paciente (models.Model):
    eps=models.ForeignKey(Eps, on_delete=models.PROTECT)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='paciente'
    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Medico (models.Model):

    Especialidad=((1, "Ortopedia"),
                  (2, "Pediatria"),
                  (3, "Urología"),)

    especialidad=models.SmallIntegerField(choices=Especialidad)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='medico'
    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Agendamiento (models.Model):

    Tipocita=((1, "Medicina General"),
              (2, "Odontologia"),
              (3, "Laboratorios"),)
    fecha=models.DateField()
    hora= models.TimeField()
    tipocita=models.SmallIntegerField(choices=Tipocita)
    medico=models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente=models.ForeignKey(Paciente, on_delete=models.PROTECT)

    class Meta:
        db_table='agendamiento'





