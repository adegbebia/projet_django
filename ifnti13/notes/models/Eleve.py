from django.db import models
from .Personne import Personne

class Eleve(Personne):
    matricule = models.CharField(max_length=100, unique=True)
    niveau = models.ForeignKey("Niveau", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
