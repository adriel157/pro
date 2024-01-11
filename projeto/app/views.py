from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Reserva
from .form import ReservaForm

class ListarView(ListView):
    model = Reserva
    template_name = 'teste/index.html'
    context_object_name = 'reservas'

class CriarView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'teste/form.html'
    success_url = reverse_lazy('listar')

class EditarView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'teste/form.html'
    success_url = reverse_lazy('listar')

class DeletarView(DeleteView):
    model = Reserva
    template_name = 'teste/deletar.html'
    success_url = reverse_lazy('listar')

class DetalharView(DetailView):
    model = Reserva
    template_name = 'teste/detalhar.html'

# Create your views here.
