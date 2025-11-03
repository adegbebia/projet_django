from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from notes.models import Eleve, Matiere

# Liste de tous les élèves
@login_required
@permission_required('notes.view_eleve', raise_exception=True)
def eleves(request):
    tous_les_eleves = Eleve.objects.all()
    return render(request, "notes/eleves.html", {"eleves": tous_les_eleves})

# Détail d'un élève
@login_required
@permission_required('notes.view_eleve', raise_exception=True)
def eleve_detail(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    matieres = Matiere.objects.filter(niveau=eleve.niveau)
    return render(request, "notes/eleve_detail.html", {"eleve": eleve, "matieres": matieres})