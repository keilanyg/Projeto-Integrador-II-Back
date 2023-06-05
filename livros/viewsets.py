from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
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
    
class emprestimo(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer
    
    