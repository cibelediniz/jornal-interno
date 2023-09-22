from django.db import models

class Edicao(models.Model):
    numero = models.IntegerField()
    data = models.DateTimeField()
    def __str__(self):
        return str(self.numero)

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

class Noticia(models.Model):
    edicao = models.ForeignKey(Edicao, default=1, on_delete = models.CASCADE)
    autor = models.ForeignKey(Autor, default=1, on_delete = models.CASCADE)
    titulo = models.CharField(max_length=250)
    conteudo = models.TextField(max_length=700)
    data_pub = models.DateTimeField()
    def __str__(self):
        return self.titulo

class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    leitor = models.ForeignKey(Leitor, default=1, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, default=1, on_delete = models.CASCADE)
    conteudo = models.CharField(max_length=300)
    data_pub = models.DateTimeField()