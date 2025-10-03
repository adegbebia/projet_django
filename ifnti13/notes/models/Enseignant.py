from django.db import models
from .Personne import Personne

class Enseignant(Personne):
#     matricule = models.CharField(max_length=100, unique=True)
    # Exemple si tu as un modèle Niveau
    # niveau = models.ForeignKey("Niveau", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
