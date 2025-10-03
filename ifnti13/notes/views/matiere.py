from django.shortcuts import render, get_object_or_404
from notes.models import Matiere

# Liste de toutes les matières
def matieres(request):
    toutes_les_matieres = Matiere.objects.all()
    return render(request, "notes/matieres.html", {"matieres": toutes_les_matieres})

# Détail d'une matière
def matiere_detail(request, id):
    matiere = get_object_or_404(Matiere, pk=id)
    return render(request, "notes/matiere_detail.html", {"matiere": matiere})
