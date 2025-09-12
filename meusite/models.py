from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    ano_publicacao = models.PositiveBigIntegerField()
    editora = models.CharField(max_length=100, blank=True, null=True)


