from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from notes.models.Eleve import Eleve
from notes.models.Matiere import Matiere

class Note(models.Model):
    valeur = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(20)],default=0
    )
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} : {self.valeur}"
