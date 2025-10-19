from django.db import models
from .Enseignant import Enseignant  

class Matiere(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    enseignant = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        related_name="matieres",
        null=True,
        blank=True
    )
    
    niveau = models.ForeignKey(
        'notes.Niveau',
        on_delete=models.CASCADE,
        related_name='matieres',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nom
