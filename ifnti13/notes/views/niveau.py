from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from notes.models import Niveau

@login_required
@permission_required('notes.view_niveau', raise_exception=True)
def niveau(request, id):
    niv = get_object_or_404(Niveau, pk=id)
    t_matiere = niv.matieres.all() 
    return render(request, "notes/niveau.html", {
        "niveau": niv,      
        "matieres": t_matiere
    })