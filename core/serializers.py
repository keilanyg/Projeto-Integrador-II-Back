from rest_framework import serializers
from core.models import User, AdministradorUser, Bibliotecario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
            
class AdministradorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorUser
        fields = '__all__'
        
        
class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecario
        fields = '__all__'