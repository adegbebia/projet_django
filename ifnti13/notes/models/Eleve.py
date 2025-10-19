from django.db import models
from .Personne import Personne
from .Niveau import Niveau
from .Matiere import Matiere

class Eleve(Personne):
    matricule = models.CharField(max_length=100, blank=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    
    # Champ ManyToMany pour les matières
    matieres = models.ManyToManyField(
        Matiere,
        blank=True,
        verbose_name="Sélectionner les matières suivies (laisser vide pour auto-associer selon le niveau)"
    )

    def __str__(self):
        return f"{self.nom} {self.prenom}"
