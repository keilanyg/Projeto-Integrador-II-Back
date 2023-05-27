from rest_framework import serializers
from livros.models import Categoria, Editora, Autor, Livros

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'