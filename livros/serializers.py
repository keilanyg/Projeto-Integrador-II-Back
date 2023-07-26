from rest_framework import serializers
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo, Devolucao
from core.serializers import UserSerializer
from core.models import User

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
    #autor = AutorSerializer(read_only = True)
    #categoria = CategoriaSerializer(read_only = True)
    #editora = EditoraSerializer(read_only = True)
    class Meta:
        model = Livro
        fields = ['nome_livro','data_cadastro', 'data_lancamento', 'quantidade', 'descricao_livro', 'categoria', 'editora',  'autor', 'cover']
        
    def quantidade_emprestado(self):
        obj =(Emprestimo.objects.filter)
        quant = self.emp
        num_emprestado = quant -1
        num_disponivel = quant - num_emprestado
        return("Quantidade de livros emprestados", num_emprestado, " Quantidade disponivel ", num_disponivel)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture']   
         
class EmprestimosSerializer(serializers.ModelSerializer):
    #nome_emprestado_usuario = UserSerializer(read_only=True)
    #livro = LivrosSerializer(read_only=True)
    class Meta:
        model = Emprestimo
        fields = ['nome_emprestado_usuario', 'livro', 'data_emprestimo']
        
        
        
class DevolucaoSerializer(serializers.ModelSerializer):
    #emprestimo = EmprestimosSerializer(read_only = True)
    class Meta:
        model = Devolucao
        fields = ['emprestimo', 'usuario_devolucao', 'data_devolucao', 'avaliacao']
        
    