from rest_framework import serializers
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo, Devolucao
from core.serializers import UserSerializer
from core.models import User
from core.serializers import UserSerializer

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
    autor_obj = serializers.SerializerMethodField('show_autor')
    editora_obj = serializers.SerializerMethodField('show_editora')
    categoria_obj = serializers.SerializerMethodField('show_categoria')
    
    class Meta:
        model = Livro
        fields = ['id','nome_livro','data_cadastro', 'data_lancamento', 'quantidade', 'descricao_livro', 'categoria', 'editora',  'autor','autor_obj', 'cover'
                  ,'editora_obj', 'categoria_obj']
        
    def show_autor(self, instance):
        autor = Autor.objects.get(id=instance.autor.id)
        serializer = AutorSerializer(autor)
        
        return serializer.data
    
    def show_editora(self, instance):
        editora = Editora.objects.get(id=instance.editora.id)
        serializer = EditoraSerializer(editora)
        
        return serializer.data
    
    def show_categoria(self, instance):
        categoria = Categoria.objects.get(id=instance.categoria.id)
        serializer = CategoriaSerializer(categoria)
        return serializer.data
    
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
    
    livro_obj = serializers.SerializerMethodField('show_livro')
    nome_emprestado_usuario_obj = serializers.SerializerMethodField('show_nome_emprestado_usuario')
    class Meta:
        model = Emprestimo
        fields = ['nome_emprestado_usuario', 'livro', 'data_emprestimo',  'livro_obj', 'nome_emprestado_usuario_obj'
                  ]
        
    def show_livro(self, instance):
        livro = Livro.objects.get(id=instance.livro.id)
        serializer = LivrosSerializer(livro)
        return serializer.data
    
    def show_nome_emprestado_usuario(self, instance):
        nome_emprestado_usuario = User.objects.get(id=instance.nome_emprestado_usuario.id)
        serializer = UserSerializer(nome_emprestado_usuario)
        return serializer.data
        
        
        
class DevolucaoSerializer(serializers.ModelSerializer):
    emprestimo_obj = serializers.SerializerMethodField('show_emprestimo')
    usuario_devolucao_obj = serializers.SerializerMethodField('show_usuario_devolucao')
    #emprestimo = EmprestimosSerializer(read_only = True)
    class Meta:
        model = Devolucao
        fields = ['emprestimo', 'usuario_devolucao', 'data_devolucao', 'avaliacao',
                  'usuario_devolucao_obj','emprestimo_obj']
        
    def show_emprestimo(self, instance):
        emprestimo = Emprestimo.objects.get(id=instance.emprestimo.id)
        serializer = EmprestimosSerializer(emprestimo)
        return serializer.data
    
    def show_usuario_devolucao(self, instance):
        usuario_devolucao = User.objects.get(id=instance.usuario_devolucao.id)
        serializer = UserSerializer(usuario_devolucao)
        return serializer.data
    