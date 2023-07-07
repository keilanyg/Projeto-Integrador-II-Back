from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo
from livros.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivrosSerializer, EmprestimosSerializer
from .filters import LivroFilter, CategoriaFilter, AutorFilter, EditoraFilter

from rest_framework.filters import SearchFilter

class categoria(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_categoria',) 
    
class editora(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filterset_class = EditoraFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_editora',)

class autor(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_autor',)

class livro(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
    filterset_class = LivroFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_livro',)
    
class emprestimo(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer
    
    