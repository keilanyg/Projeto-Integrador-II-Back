from rest_framework import serializers
from core.models import User, Bibliotecario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
            
        
        
class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecario
        fields = '__all__'