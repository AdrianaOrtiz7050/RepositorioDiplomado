from django.shortcuts import render
from    django.views.generic import ListView, FormView, UpdateView,  DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Agendamiento, Eps, Profile, Paciente, Medico
from .forms import Formulariocita, Formularioeps, Formulariomedico, Formulariopaciente, Formularioprofile
# Create your views here.

class Viendocitas(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_agendamiento'
    login_url = 'login'
    model=Agendamiento
    template_name = 'vercita.html'

    def get_queryset(self):
        queryset = super(Viendocitas, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset = queryset.filter(paciente__user=self.request.user)
        if self.request.user.groups.filter(name="Medico").exists():
            queryset = queryset.filter(medico__user=self.request.user)

        return queryset

class Insertarcita(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_agendamiento'
    login_url = 'login'
    form_class=Formulariocita
    template_name = 'insertarcita.html'
    success_url='/vercita'
    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Eliminarcita(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_agendamiento'
    login_url = 'login'
    model = Agendamiento
    template_name = 'elicita.html'
    success_url = '/vercita'

class Editarcita(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_agendamiento'
    login_url = 'login'
    model = Agendamiento
    template_name = 'editarcita.html'
    success_url = '/vercita'
    form_class = Formulariocita
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Viendoeps(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_eps'
    login_url = 'login'
    model = Eps
    template_name = 'vereps.html'

class Editareps(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_eps'
    login_url = 'login'
    model = Eps
    template_name = 'editareps.html'
    success_url = '/vereps'
    form_class = Formularioeps
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Insertareps(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_eps'
    login_url = 'login'
    form_class=Formularioeps
    template_name = 'insertareps.html'
    success_url='/vereps'
    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Eliminareps(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_eps'
    login_url = 'login'
    model = Eps
    template_name = 'elieps.html'
    success_url = '/vereps'

class Viendoperfil(LoginRequiredMixin, ListView):
    permission_required = 'citas.view_profile'
    login_url = 'login'
    model=Profile
    template_name = 'verperfil.html'

class Insertarperfil(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_profile'
    login_url = 'login'
    form_class=Formularioprofile
    template_name = 'insertarperfil.html'
    success_url='/verperfil'
    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Eliminarperfil(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_profile'
    login_url = 'login'
    model = Profile
    template_name = 'eliperfil.html'
    success_url = '/verperfil'

class Editarperfil(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_profile'
    login_url = 'login'
    model = Profile
    template_name = 'editarperfil.html'
    success_url = '/verperfil'
    form_class = Formulariomedico
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Viendopaciente(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'verpaciente.html'

class Insertarpaciente(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_paciente'
    login_url = 'login'
    form_class=Formulariopaciente
    template_name = 'insertarpaciente.html'
    success_url='/verpaciente'
    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Eliminarpaciente(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'elipaciente.html'
    success_url = '/verpaciente'

class Editarpaciente(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'editarpaciente.html'
    success_url = '/verpaciente'
    form_class = Formulariopaciente
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Viendomedico (PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_medico'
    login_url = 'login'
    model = Medico
    template_name = 'vermedico.html'

class Insertarmedico(LoginRequiredMixin, FormView):
    permission_required = 'citas.add_medico'
    login_url = 'login'
    form_class=Formulariomedico
    template_name = 'insertarmedico.html'
    success_url='/vermedico'
    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Eliminarmedico(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_medico'
    login_url = 'login'
    model = Medico
    template_name = 'elimedico.html'
    success_url = '/vermedico'

class Editarmedico(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_medico'
    login_url = 'login'
    model = Medico
    template_name = 'editarmedico.html'
    success_url = '/vermedico'
    form_class = Formulariomedico
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

