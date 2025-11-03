from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from notes.forms.Eleveform import EleveForm

@login_required
@permission_required('notes.add_eleve', raise_exception=True)
def add_eleve(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:eleves')
        else:
            print(form.errors) 
    else:
        form = EleveForm()
    return render(request, 'notes/add_eleve.html', {'form': form})