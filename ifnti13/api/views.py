from django.contrib.auth.models import User
from rest_framework import routers, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

@api_view(["GET"])
def users_api_view(request):
    try:
        # Récupérer tous les utilisateurs
        users = User.objects.all()
        users_data = UserSerializer(users, many=True).data
        
        return Response(data=users_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        # En cas d'erreur, renvoyer un message d'erreur
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)