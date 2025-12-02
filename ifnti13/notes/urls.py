from django.urls import path
from django.contrib.auth import views as auth_views
from notes.views import index, eleve, matiere, niveau, statistique, note, enseignant
from notes.views import add_eleve, update_eleve, add_enseignant, update_enseignant,jpl

app_name = "notes"

urlpatterns = [
   

    # Page d'accueil
    path('', index.index, name='index'),
    
    #jpl
    path("jpl", jpl.jpl_view, name="jpl"),

    # URLs d'authentification
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ÉLÈVES
    path('eleves/', eleve.eleves, name='eleves'),
    path('eleve/<int:id>/', eleve.eleve_detail, name='eleve'),
    path('add_eleve/', add_eleve.add_eleve, name='add_eleve'),
    path('eleve/update/<int:id>/', update_eleve.update_eleve, name='update_eleve'),

    # ENSEIGNANTS
    path('enseignants/', enseignant.enseignant, name='enseignants'), 
    path('add_enseignant/', add_enseignant.add_enseignant, name='add_enseignant'),
    path('update_enseignant/<int:id>/', update_enseignant.update_enseignant, name='update_enseignant'),

    # MATIÈRES
    path('matieres/', matiere.matieres, name='matieres'),
    path('matiere/<int:id>/', matiere.matiere_detail, name='matiere'),

    # NIVEAUX & STATISTIQUES
    path('niveau/<int:id>/', niveau.niveau, name='niveau'),
    path('statistiques/', statistique.statistique, name='statistique'),
    path('statistiques/<int:id_niveau>/', statistique.statistique, name='statistique_niveau'),

    # NOTES
    path('add_note/<int:eleve_id>/<int:matiere_id>/', note.add_note, name='add_note'),
]