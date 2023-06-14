from rest_framework import serializers
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo

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
        model = Livro
        fields = '__all__'
        
class EmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = "__all__"
        
        
        