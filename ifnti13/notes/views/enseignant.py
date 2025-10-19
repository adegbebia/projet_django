from django.shortcuts import render
from notes.models import Enseignant

def enseignant(request):
    tous_les_enseignants = Enseignant.objects.all()
    return render(request, 'notes/enseignant.html', {'enseignants': tous_les_enseignants})
