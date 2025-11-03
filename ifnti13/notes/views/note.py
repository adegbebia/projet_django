from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Eleve, Matiere, Note
from notes.forms.Noteform import NoteForm

@login_required
@permission_required('notes.add_note', raise_exception=True)
def add_note(request, eleve_id, matiere_id):
    eleve = get_object_or_404(Eleve, id=eleve_id)
    matiere = get_object_or_404(Matiere, id=matiere_id)

    
    if matiere not in eleve.niveau.matieres.all():
        raise Exception("L'élève ne suit pas cette matière.")

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.eleve = eleve
            note.matiere = matiere
            note.save()
            return redirect('notes:eleve_detail', eleve_id=eleve.id)
    else:
        form = NoteForm()

    return render(request, 'add_note.html', {'form': form, 'eleve': eleve, 'matiere': matiere})