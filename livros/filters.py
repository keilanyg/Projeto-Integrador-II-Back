from django_filters import rest_framework as filters
from django_filters import FilterSet
from datetime import timezone, timedelta
from dateutil.relativedelta import relativedelta 

from .models import Livro, Categoria, Editora, Autor, Emprestimo
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from .serializers import LivrosSerializer, CategoriaSerializer, AutorSerializer, EditoraSerializer

class LivroFilter(FilterSet):
    class Meta:
        model = Livro
        fields = {
            'nome_livro': ['exact', 'icontains'],
            'autor': ['exact'],
            'editora': ['exact'],
        }
        
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = LivroFilter
    search_fields = ['nome_livro']
        
class CategoriaFilter(FilterSet):
    class Meta:
        model = Categoria
        fields = {
            'nome_categoria': ['exact', 'icontains'],
        }
        
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CategoriaFilter
    search_fields = ['nome_categoria']

class AutorFilter(FilterSet):
    class Meta:
        model = Autor
        fields = {
            'nome_autor': ['exact','icontains'],
        }
        
class AutorViewSet(viewsets.ModelViewSet):
    #permission_classes=[permissions.AllowAny] #sem autenticação para acesso a API
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AutorFilter
    search_fields = ['autor']
    
class EditoraFilter(FilterSet):
    class Meta:
        model = Editora
        fields = {
            'nome_editora': ['exact','icontains'],
        }
        
class EditoraViewSet(viewsets.ModelViewSet):
    #permission_classes=[permissions.AllowAny] #sem autenticação para acesso a API
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = EditoraFilter
    search_fields = ['editora']
    
class EmprestimoFilter(filters.FilterSet):
    period = filters.CharFilter(method='filter_by_period')

    def filter_by_period(self, queryset, name, value):
        today = timezone.now().date()
        if value == 'day':
            return queryset.filter(data_emprestimo=today)
        elif value == 'week':
            week_start = today - timedelta(days=today.weekday())
            week_end = week_start + timedelta(days=6)
            return queryset.filter(data_emprestimo__range=[week_start, week_end])
        elif value == 'month':
            month_start = today.replace(day=1)
            month_end = (month_start + relativedelta(months=1)) - timedelta(days=1)
            return queryset.filter(data_emprestimo__range=[month_start, month_end])
        return queryset

    class Meta:
        model = Emprestimo
        fields = ['period']