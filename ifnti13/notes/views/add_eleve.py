from django.shortcuts import render, redirect
from notes.forms.Eleveform import EleveForm

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
