from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
import datetime 

from livros.models import *
from livros.serializers import *
from .filters import *
from core.models import User
from core.permissions import IsBibliotecario, IsAdministradores, IsUsuarios

class CategoriaViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsBibliotecario]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_categoria',)

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filterset_class = EditoraFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_editora',)

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_autor',)

class LivroViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
    filterset_class = LivroFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_livro',)

class EmprestimoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer
    filter_class = EmprestimoFilter

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def quantidade_emprestado(self):
        quant = self.queryset.count()
        num_emprestado = quant - 1
        num_disponivel = quant - num_emprestado
        return Response({
            "Quantidade de livros emprestados": num_emprestado,
            "Quantidade disponivel": num_disponivel
        })
    
    def __str__(self):
        return f"LIVRO: {self.livro} - USUÁRIO: {self.nome_emprestado_usuario}"

class DevolucaoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer
    filter_class = DevolucaoFilter
    
    def devolver(self, request, *args, **kwargs):
        try:
            emprestimo = Emprestimo.objects.get(pk=kwargs['pk'])
            Devolucao.objects.create(
                emprestimo=emprestimo,
                data_devolucao=datetime.date.today(),
                usuario_devolucao=request.user
            )
            emprestimo.delete()

            return Response("Livro devolvido com sucesso!")
        except Emprestimo.DoesNotExist:
            return Response("Empréstimo não encontrado.", status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        emprestimo_obj = Emprestimo.objects.get(id=request.data["emprestimo"])
        emprestimo_obj.delete()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
