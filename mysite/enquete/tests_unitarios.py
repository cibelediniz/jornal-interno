import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Pergunta

class PerguntaModelTest(TestCase):
    def test_pub_recentemente_com_pergunta_no_futuro(self):
        """
        Ao invocar o método com data no futuro a resposta DEVE ser False
        """
        data = timezone.now() + datetime.timedelta(seconds=1)
        pergunta = Pergunta(data_pub = data)
        self.assertIs(pergunta.pub_recentemente(), False)

    def test_pub_recentemente_com_pergunta_alem_das_48hs(self):
        """
        Para uma pergunta com data anterior a 48hs a resposta DEVE ser False
        """
        data = timezone.now() - datetime.timedelta(hours=48, seconds=1)
        pergunta = Pergunta(data_pub = data)
        self.assertIs(pergunta.pub_recentemente(), False)

    def test_pub_recentemente_com_pergunta_dentro_das_48hs(self):
        """
        Para pergunta com data dentro das 48hs a resposta DEVE ser True
        """
        data = timezone.now() - datetime.timedelta(
            hours=47, minutes=59, seconds=59
        )
        pergunta = Pergunta(data_pub = data)
        self.assertIs(pergunta.pub_recentemente(), True)
