import os
import django
import random
from datetime import datetime

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifnti13.settings')
django.setup()

# Importer les modèles
from notes.models import Eleve, Niveau, Matiere, Note


Note.objects.all().delete()
Eleve.objects.all().delete()
Niveau.objects.all().delete()
Matiere.objects.all().delete()  


niveaux = [Niveau.objects.create(nom=f'L{i}') for i in range(3)]


matieres = [Matiere.objects.create(nom=f'Matiere{i}') for i in range(3)]


eleves = []
for i in range(10):
    sexe = random.choice(['M', 'F']) 
    niveau = random.choice(niveaux)  
    eleve = Eleve.objects.create(
        matricule=f"MA{i}",
        nom=f"Nom{i}",
        prenom=f"Prenom{i}",
        sexe=sexe, 
        date=datetime(2005, 1, 1),
        niveau=niveau  
    )
    eleves.append(eleve)  


for eleve in eleves:
    for matiere in matieres:
        Note.objects.create(
            valeur=random.uniform(0, 20),  
            matiere=matiere,
            eleve=eleve
        )