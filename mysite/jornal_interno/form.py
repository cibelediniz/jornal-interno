from django import forms
from .models import Edicao, Noticia, Comentario

class EdForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['numero', 'data']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['edicao', 'autor', 'titulo', 'conteudo', 'data_pub']

class ComentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['leitor', 'noticia', 'conteudo', 'data_pub']
