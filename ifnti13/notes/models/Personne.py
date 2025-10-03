from django.db import models

class Personne(models.Model):
    SEXE = { "F": "Feminin", "M": "Masculin" }
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=SEXE)
    date = models.DateField()

    class Meta:
        abstract = True