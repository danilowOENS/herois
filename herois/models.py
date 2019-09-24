from django.db import models

# Create your models here.
from habilidade.models import Habilidade
from universo.models import Universo

class Herois(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    habilidade_heroi = models.ManyToManyField(
        Habilidade,
        related_name='habilidade_heroi'
    )
    universo_heroi = models.ForeignKey(
        Universo,
        on_delete=models.CASCADE,
        related_name='universo_heroi'
    )