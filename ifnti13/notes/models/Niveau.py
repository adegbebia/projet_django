from django.db import models
from .Matiere import Matiere
class Niveau(models.Model):
    nom = models.CharField(max_length=2, unique=True)
    matieres = models.ManyToManyField(Matiere)