from django.contrib import admin
from .models import Pergunta, Alternativa

admin.site.site_header = 'CRUD das Aplicações de DSWeb 2023.1'

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['enunciado']}),
        ('Informações da data', {'fields': ['data_pub']}),
    ]
    inlines = [AlternativaInline]
    list_display = [
        'enunciado', 'id', 'data_pub', 'publicada_recentemente'
    ]
    list_filter = ['data_pub']
    search_fields = ['enunciado']

admin.site.register(Pergunta, PerguntaAdmin)
