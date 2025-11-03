from django.contrib import admin
from .models import Eleve, Niveau, Matiere, Note
from .forms.Eleveform import EleveForm


@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    form = EleveForm

    # Liste et apparence
    list_display = ('nom', 'prenom', 'sexe', 'niveau', 'date')
    list_display_links = ('nom', 'prenom')
    list_editable = ('niveau',)

    # Filtres et recherche
    list_filter = ('niveau', 'sexe')
    search_fields = ('nom', 'prenom')
    date_hierarchy = 'date'

    # Options générales
    list_per_page = 10
    empty_value_display = '— Non renseigné —'
    save_on_top = True
    save_as = True

    # Champs du formulaire
    fields = ('nom', 'prenom', 'sexe', 'niveau', 'date')
   

     # Pour les relations
    raw_id_fields = ('niveau',)


# Autres modèles sans personnalisation particulière
@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    pass

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
