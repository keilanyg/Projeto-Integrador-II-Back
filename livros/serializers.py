from rest_framework import serializers
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo, Devolucao

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
    autor = AutorSerializer(read_only = True)
    categoria = CategoriaSerializer(read_only = True)
    editora = EditoraSerializer(read_only = True)
    class Meta:
        model = Livro
        fields = ['nome_livro','data_cadastro', 'data_lancamento', 'quantidade', 'descricao_livro', 'categoria', 'editora',  'autor', 'cover']
        
    def quantidade_emprestado(self):
        obj =(Emprestimo.objects.filter)
        quant = self.emp
        num_emprestado = quant -1
        num_disponivel = quant - num_emprestado
        return("Quantidade de livros emprestados", num_emprestado, " Quantidade disponivel ", num_disponivel)
        
class EmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = "__all__"
        
        
class DevolucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucao
        fields = "__all__"