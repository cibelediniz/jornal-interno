import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Pergunta

def criar_pergunta(texto, dias):
    """
    Cria uma instância de pergunta com um dado enunciado e uma data
    """
    data = timezone.now() + datetime.timedelta(days=dias)
    return Pergunta.objects.create(enunciado=texto, data_pub=data)

class DetalhesViewTest(TestCase):
    def test_com_pergunta_no_futuro(self):
        """
        Ao tentar exibir detalhes de pergunta no futuro recebemos um 404
        """
        pergunta = criar_pergunta('Pergunta futura', 5)
        url = reverse('enquete:detalhes', args=(pergunta.id,))
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 404)

    def test_com_pergunta_no_passado(self):
        """
        Exibe normalmente os detalhes de pergunta no passado
        """
        pergunta = criar_pergunta('Pergunta no passado', -1)
        url = reverse('enquete:detalhes', args=(pergunta.id,))
        resposta = self.client.get(url)
        self.assertContains(resposta, pergunta.enunciado)

class IndexViewTest(TestCase):
    def test_sem_perguntas_cadastradas(self):
        """
        Não havendo perguntas é exibida uma mensagem correspondente
        """
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(
            resposta.context['pergunta_list'], []
        )

    def test_pergunta_com_data_no_passado(self):
        """
        Pergunta com data no passado são exibidas normalmente
        """
        criar_pergunta('Pergunta no passado', -1)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(
            resposta.context['pergunta_list'],
            ['<Pergunta: Pergunta no passado>']
        )

    def test_pergunta_com_data_futura(self):
        """
        Pergunta com data no futuro não deve ser exibida na Index
        """
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(
            resposta.context['pergunta_list'], []
        )

    def test_com_pergunta_no_passado_outra_no_futuro(self):
        """
        Só deve ser exibida a pergunta com data no passado
        """
        criar_pergunta('Pergunta no passado', -1)
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(
            resposta.context['pergunta_list'],
            ['<Pergunta: Pergunta no passado>']
        )

    def test_com_duas_perguntas_no_passado(self):
        """
        As pergunta com data no passado são exibidas ordenadas
        """
        criar_pergunta('Pergunta no passado 1', -10)
        criar_pergunta('Pergunta no passado 2', -5)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertQuerysetEqual(
            resposta.context['pergunta_list'],
            ['<Pergunta: Pergunta no passado 2>',
            '<Pergunta: Pergunta no passado 1>']
        )