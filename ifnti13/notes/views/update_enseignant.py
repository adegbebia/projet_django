from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Enseignant
from notes.forms.Enseignantform import EnseignantForm

@login_required
@permission_required('notes.change_enseignant', raise_exception=True)
def update_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('notes:enseignants')
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'notes/update_enseignant.html', {'form': form, 'enseignant': enseignant})