from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Eleve
from notes.forms.Eleveform import EleveForm

def update_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    if request.method == 'POST':
        form = EleveForm(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            return redirect('notes:eleves')
    else:
        form = EleveForm(instance=eleve)
    return render(request, 'notes/update_eleve.html', {'form': form, 'eleve': eleve})
