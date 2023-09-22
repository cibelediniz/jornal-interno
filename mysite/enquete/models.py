import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    enunciado = models.CharField(max_length = 150)
    data_pub = models.DateTimeField('Data de publicação')
    def __str__(self):
        return self.enunciado
    def publicada_recentemente(self):
        marco_48hs = timezone.now() - datetime.timedelta(hours=48)
        agora = timezone.now()
        return marco_48hs <= self.data_pub <= agora
    publicada_recentemente.admin_order_field = 'data_pub'
    publicada_recentemente.boolean = True
    publicada_recentemente.short_description = 'Recente?'

class Alternativa(models.Model):
    texto = models.CharField(max_length = 80)
    quant_votos = models.IntegerField('Quantidade de votos', default = 0)
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
    def __str__(self):
        return self.texto
