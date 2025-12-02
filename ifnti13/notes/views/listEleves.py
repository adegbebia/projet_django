from django.http import HttpResponse
from django.shortcuts import render
from notes.models import Eleve  # Remplacez par le nom de votre modèle
from notes.Templating_ifnti.controlleur import generate_pdf  # Importez votre fonction de génération PDF

def listEleves(request):
    # Récupérer tous les élèves depuis la base de données
    eleves = Eleve.objects.all()
    
    # Créer le contexte à passer à la fonction de génération PDF
    context = {'eleves': eleves}

    # Appeler la fonction pour générer le PDF
    generate_pdf(context)

    # Retourner une réponse (optionnel, selon l'implémentation de generate_pdf)
    return HttpResponse("PDF généré avec succès.")