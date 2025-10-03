from django.db import models
from .Matiere import Matiere
from .Eleve import Eleve

class Note(models.Model):
    valeur = models.FloatField(null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)