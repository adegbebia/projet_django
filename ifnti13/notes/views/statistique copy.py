
from django.shortcuts import render 
from django.db.models import Count, Avg
from notes.models import Eleve
from notes.models import Enseignant
from notes.models import Note
from notes.models import  Matiere
from notes.models import  Niveau


def statistique(request):


    ##1

    total_eleves=Eleve.objects.count()
    total_enseignants=Enseignant.objects.count()
    total_matieres=Matiere.objects.count()
    total_notes=Note.objects.count()

    
    ##2
    moyennes_eleves = []
    eleves=Eleve.objects.all()
    for e in eleves:
        moyennes_eleve=e.note.all()
    ##3
    moyennes_matieres = (
        Matiere.objects.values('nom')
        .annotate(moyenne=Avg('valeur'))
        .order_by('nom')
    )
    ##4
   


    


    # ##5
    # stats_niveaux = (
    #    Niveau.objects
    #     .annotate(
    #         nombre_eleves=Count('eleve'),
    #         moyenne_niveau=Avg('note')
    #     )
    #     .values('nom', 'nombre_eleves', 'moyenne_niveau')
    # )

    # from django.db.models import Count, Avg

    stats_niveaux = (
        Niveau.objects
        .annotate(
            nombre_eleves=Count('eleve'),
            moyenne_niveau=Avg('eleve__note__valeur')  
        )
        .values('nom', 'nombre_eleves', 'moyenne_niveau')
    )

    contexte = {
        'total_eleves': total_eleves,
        'total_enseignants': total_enseignants,
        'total_matieres': total_matieres,
        'total_notes': total_notes,
        'moyennes_eleves': moyennes_eleves,
        'moyennes_matieres': moyennes_matieres,
        #'top_eleves': top_eleves,
        #'stats_niveaux': stats_niveaux,
    }

    return render(request, 'notes/statistiques.html', contexte)
    








