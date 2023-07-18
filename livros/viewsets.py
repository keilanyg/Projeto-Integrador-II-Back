from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo, Devolucao
from livros.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivrosSerializer, EmprestimosSerializer, DevolucaoSerializer
from .filters import LivroFilter, CategoriaFilter, AutorFilter, EditoraFilter, EmprestimoFilter
from rest_framework import generics
from rest_framework.filters import SearchFilter
import datetime
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from core.permissions import IsBibliotecario, IsAdministradores, IsUsuarios
from rest_framework.permissions import IsAuthenticated
from notifications.signals import notify


class categoria(ModelViewSet):
    permission_classes = [IsAuthenticated & (IsBibliotecario)]
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
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
    filterset_class = LivroFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_livro',)
    
    def quantidade_emprestado(quantidade):
        pass 
      
class emprestimo(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer
    filter_class = EmprestimoFilter
    
    """def notificacao(request):
        
        user = User.objects.get(id = id)
        notify.send(request.user, recipent="user")"""
        

class devolucao(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        emprestimo_obj = Emprestimo.objects.get(id=request.data["emprestimo"])
        emprestimo_obj.delete()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    
    #filter_class = DevolucaoFilter
    def devolver(self, livro):
        devolucao = Devolucao.objects.create(emprestimo=self, data_devolucao=datetime.date.today(), usuario_devolucao=self.nome_emprestado_usuario)
        #emprestimo = Emprestimo.objects.get(pk=self.pk)
        if Emprestimo.objects.filter(pk=self.pk).exists():
            livro.delete()
    