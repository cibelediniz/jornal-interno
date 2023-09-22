from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from .models import Pergunta, Alternativa

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista_perguntas = Pergunta.objects.filter(
            data_pub__lte = timezone.now()
        ).order_by('-data_pub')
        contexto = {'pergunta_list': lista_perguntas}
        return render(request, 'enquete/index.html', contexto)

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        if pergunta.data_pub > timezone.now():
            raise Http404('No Pergunta matches the given query.')
        return render(
            request, 'enquete/pergunta_detail.html', {'pergunta': pergunta}
        )

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        return render(
            request, 'enquete/resultado.html', {'pergunta': pergunta}
        )

class VotacaoView(View):
    def post(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        try:
            id_alternativa = request.POST['escolha']
            alt_selecionada = pergunta.alternativa_set.get(pk=id_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'pergunta': pergunta,
                'error': 'Você precisa selecionar uma alternativa válida!'
            }
            return render(request, 'enquete/pergunta_detail.html', contexto)
        else:
            alt_selecionada.quant_votos += 1
            alt_selecionada.save()
            return HttpResponseRedirect(
                reverse('enquete:resultado',args=(pergunta.id,))
            )


'''
### Primeira versão da visão INDEX
def index(request):
    lista_perguntas = Pergunta.objects.all()
    resposta = '<br/> '.join([p.enunciado for p in lista_perguntas])
    return HttpResponse(resposta)

### Segunda versão da visão INDEX
def index(request):
    lista_perguntas = Pergunta.objects.order_by('-data_pub')
    template = loader.get_template('enquete/index.html')
    contexto = {'lista_perguntas': lista_perguntas}
    return HttpResponse(template.render(contexto, request))

### Terceira versão da visão INDEX
def index(request):
    lista_perguntas = Pergunta.objects.order_by('-data_pub')
    contexto = {'lista_perguntas': lista_perguntas}
    return render(request, 'enquete/index.html', contexto)

### Quarta versão da visão INDEX
class IndexView(generic.ListView):
    def get_queryset(self):
        return Pergunta.objects.order_by('-data_pub')

########################################
### Primeira versão da visão de DETALHES
def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk = pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404("Identificador de enquete inválido!")
    return render(request, 'enquete/detalhes.html', {'pergunta': pergunta})

### Segunda versão da visão de DETALHES
def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'enquete/detalhes.html', {'pergunta': pergunta})

### Terceira versão da visão de DETALHES
class DetalhesView(generic.DetailView):
    model = Pergunta

##########################################
### Primeira versão da visão de RESULTADOS
def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'enquete/resultado.html', {'pergunta': pergunta})

### Segunda versão da visão de RESULTADOS
class ResultadoView(generic.DetailView):
    model = Pergunta
    template_name = 'enquete/resultado.html'

#######################################
### Primeira versão da visão de VOTAÇÃO
def votacao(request, pk):
    pergunta = get_object_or_404(Pergunta, pk = pk)
    try:
        id_alternativa = request.POST['escolha']
        alt_selecionada = pergunta.alternativa_set.get(pk=id_alternativa)
    except (KeyError, Alternativa.DoesNotExist):
        contexto = {
            'pergunta': pergunta,
            'error': 'Você precisa selecionar uma alternativa válida!'
        }
        return render(request, 'enquete/detalhes.html', contexto)
    else:
        alt_selecionada.quant_votos += 1
        alt_selecionada.save()
        return HttpResponseRedirect(
            reverse('enquete:resultado',args=(pergunta.id,))
        )
'''