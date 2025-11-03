from django.db import models
from django.contrib.auth.models import User

class Personne(models.Model):
    SEXE = { "F": "Feminin", "M": "Masculin" }
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=SEXE)
    date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True