from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'criado_em']
    search_fields = ['nome', 'email', 'telefone']
    list_filter = ['criado_em']
