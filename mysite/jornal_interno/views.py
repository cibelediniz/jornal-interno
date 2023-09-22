from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Edicao, Noticia, Comentario
from .form import EdForm, NoticiaForm, ComentForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        edicao_mais_recente = Edicao.objects.latest('data')
        noticias = Noticia.objects.filter(edicao=edicao_mais_recente)
        return render(
            request, 'jornalinterno/index.html',
            {'edicao_mais_recente': edicao_mais_recente, 'noticias': noticias}
        )


class ListarEdicoesView(View):
    def get(self, request, *args, **kwargs):
        edicoes = Edicao.objects.all()
        query = request.GET.get('qr', '')
        if query:
            noticias = Noticia.objects.filter(titulo__icontains=query)
        else:
            noticias = Noticia.objects.all()
        return render(
            request, 'jornalinterno/listar_edicoes.html',
            {'edicoes': edicoes, 'noticias': noticias, 'query': query}
        )


class PaginaEdicaoView(View):
    def get(self, request, *args, **kwargs):
        edicao = get_object_or_404(Edicao, pk=kwargs['pk'])
        query = request.GET.get('qr', '')
        if query:
            noticias = Noticia.objects.flter(titulo__icontains=query, edicao=edicao)
        else:
            noticias = Noticia.objects.filter(edicao=edicao)
        return render(
            request, 'jornalinterno/pagina_edicao.html',
            {'edicao': edicao, 'noticias': noticias}
        )


class PaginaNoticiaView(View):
    def get(self, request, *args, **kwargs):
        noticia = get_object_or_404(Noticia, pk=kwargs['pk'])
        comentarios = Comentario.objects.filter(noticia=noticia).select_related('leitor')
        return render(
            request, 'jornalinterno/pagina_noticia.html',
            {'noticia': noticia, 'comentarios': comentarios}
        )


class AddEdView(View):
    def get(self, request, *args, **kwargs):
        form = EdForm()
        return render(request, 'jornalinterno/add_ed.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = EdForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('jornalinterno:listar_edicoes')
        return render(request, 'jornalinterno/add_ed.html', {'form': form})


class AddNoticiaView(View):
    def get(self, request, *args, **kwargs):
        form = NoticiaForm()
        edicoes = Edicao.objects.all()
        return render(request, 'jornalinterno/add_noticia.html', {'form': form, 'edicoes': edicoes})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NoticiaForm(request.POST)
            if form.is_valid():
                noticia = form.save(commit=False)
                edicao_id = request.POST.get('edicao')
                try:
                    edicao = Edicao.objects.get(pk=edicao_id)
                except Edicao.DoesNotExist:
                    edicao = None
                noticia.edicao = edicao
                noticia.save()
                return redirect('jornalinterno:listar_edicoes')
        return render(request, 'jornalinterno/add_noticia.html', {'form': form})


class AddComentView(View):
    def get(self, request, *args, **kwargs):
        form = ComentForm()
        return render(request, 'jornalinterno/add_coment.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ComentForm(request.POST)
            if form.is_valid():
                form.save()
                noticia_id = kwargs['noticia_id']
                return redirect('jornalinterno:pagina_noticia', pk=noticia_id)
        return render(request, 'jornalinterno/add_coment.html', {'form': form})