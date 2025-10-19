
from django.shortcuts import render 
from django.db.models import Count, Avg
from notes.models import Eleve
from notes.models import Enseignant
from notes.models import Note
from notes.models import  Matiere
from notes.models import  Niveau

def statistiques_niveau(request, id):
    from django.db.models import Avg, Count
    niveau = Niveau.objects.get(pk=id)
    eleves = Eleve.objects.filter(niveau=niveau)
    moyennes_eleves = (
        Note.objects.filter(eleve__in=eleves)
        .values('nom', 'prenom')
        .annotate(moyenne=Avg('note'))
    )
    moyenne_niveau = moyennes_eleves.aggregate(moyenne=Avg('moyenne'))['moyenne']
    nombre_eleves = eleves.count()

    contexte = {
        'niveau': niveau,
        'moyennes_eleves': moyennes_eleves,
        'moyenne_niveau': moyenne_niveau,
        'nombre_eleves': nombre_eleves,
    }
    return render(request, 'notes/statistiques_niveau.html', contexte)

