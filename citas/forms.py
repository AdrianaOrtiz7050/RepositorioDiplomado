from django import forms
from .models import Agendamiento, Eps, Profile, Paciente, Medico

class Formulariocita(forms.ModelForm):
    class Meta:
        model=Agendamiento
        fields= '__all__'

class Formularioeps(forms.ModelForm):
    class Meta:
        model=Eps
        fields= '__all__'

class Formulariomedico(forms.ModelForm):
    class Meta:
        model=Medico
        fields= '__all__'

class Formulariopaciente(forms.ModelForm):
    class Meta:
        model=Paciente
        fields= '__all__'

class Formularioprofile(forms.ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'


