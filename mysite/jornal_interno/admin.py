from django.contrib import admin
from .models import Edicao, Autor, Noticia, Comentario, Leitor

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')

admin.site.register(Edicao)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Leitor)