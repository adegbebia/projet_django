from django.shortcuts import render, get_object_or_404
from notes.models import Niveau

def niveau(request, id):
    niv = get_object_or_404(Niveau, pk=id)
    t_matiere = niv.matieres.all() 
    return render(request, "notes/niveau.html", {
        "niveau": niv,      
        "matieres": t_matiere
    })
