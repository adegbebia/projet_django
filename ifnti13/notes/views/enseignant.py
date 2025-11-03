from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from notes.models import Enseignant

@login_required
@permission_required('notes.view_enseignant', raise_exception=True)
def enseignant(request):
    tous_les_enseignants = Enseignant.objects.all()
    return render(request, 'notes/enseignant.html', {'enseignants': tous_les_enseignants})