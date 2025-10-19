from django import forms
from ..models import Eleve, Matiere

class EleveForm(forms.ModelForm):
    matieres = forms.ModelMultipleChoiceField(
        queryset=Matiere.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Sélectionner les matières suivies (laisser vide pour auto-associer selon le niveau)"
    )

    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'sexe', 'date', 'matricule', 'niveau','matieres']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if any(char.isdigit() for char in nom):
            raise forms.ValidationError("Le nom ne peut pas contenir de chiffres.")
        return nom

    def clean_prenom(self):
        prenom = self.cleaned_data.get('prenom')
        if any(char.isdigit() for char in prenom):
            raise forms.ValidationError("Le prénom ne peut pas contenir de chiffres.")
        return prenom

    def clean(self):
        cleaned_data = super().clean()
        niveau = cleaned_data.get("niveau")
        matieres = cleaned_data.get("matieres")
        if matieres:
            for matiere in matieres:
                if matiere.niveau != niveau:
                    raise forms.ValidationError(
                        f"La matière {matiere} ne correspond pas au niveau choisi."
                    )
        return cleaned_data

    def save(self, commit=True):
        # Récupère l'instance sans l'enregistrer
        instance = super().save(commit=False)

        # Génération automatique du matricule
        nom_part = instance.nom[:2].upper()
        prenom_part = instance.prenom[:2].upper()
        sexe_part = instance.sexe.upper()[0]
        annee_naissance = instance.date.year
        instance.matricule = f"{nom_part}{prenom_part}{sexe_part}{annee_naissance}"

        # Enregistre l'instance
        if commit:
            instance.save()

        # Gestion automatique des matières si le champ est vide
        if not self.cleaned_data.get('matieres'):
            matieres_niveau = Matiere.objects.filter(niveau=instance.niveau)
            instance.matieres.set(matieres_niveau)
        else:
            instance.matieres.set(self.cleaned_data['matieres'])

        return instance
