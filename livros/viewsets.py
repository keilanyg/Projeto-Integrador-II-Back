from rest_framework.viewsets import ModelViewSet
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo
from livros.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivrosSerializer, EmprestimosSerializer

class categoria(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class editora(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class autor(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class livro(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
    
class emprestimo(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer