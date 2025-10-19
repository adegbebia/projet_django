from django.contrib import admin
from .models import Eleve, Niveau, Matiere, Note  
from .forms.Eleveform import EleveForm 



class EleveAdmin(admin.ModelAdmin):
    form = EleveForm

# Enregistrer les modèles
admin.site.register(Eleve, EleveAdmin)
admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Note)
