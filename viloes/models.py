from django.db import models

# Create your models here.

from habilidade.models import Habilidade
from universo.models import Universo

class Viloes(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    habilidade = models.ManyToManyField(
        Habilidade,
        related_name='habilidade'
    )
    universo_viloes= models.ForeignKey(
        Universo,
        on_delete=models.CASCADE,
        related_name='universo_viloes'
    )
