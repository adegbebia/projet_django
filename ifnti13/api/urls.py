from api.views import users_api_view  # Importer la fonction de vue
from django.urls import path

urlpatterns = [
    path('users/', users_api_view, name='users_api_view'),  # Assurez-vous que c'est une fonction de vue
]