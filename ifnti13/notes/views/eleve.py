from django.shortcuts import render, get_object_or_404
from notes.models import Eleve

# Liste de tous les élèves
def eleves(request):
    tous_les_eleves = Eleve.objects.all()
    return render(request, "notes/eleves.html", {"eleves": tous_les_eleves})

# Détail d'un élève
def eleve_detail(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve_detail.html", {"eleve": eleve})
