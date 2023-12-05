from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('nome_empresa','cnpj','quitado',)

# Register your models here.
