from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from notes.forms.Enseignantform import EnseignantForm

@login_required
@permission_required('notes.add_enseignant', raise_exception=True)
def add_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'notes/add_enseignant.html', {'form': form})