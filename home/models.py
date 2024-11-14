from django.db import models

class Artigo(models.Model):
    conteudo_artigo = models.TextField()
