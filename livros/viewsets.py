import requests
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
import datetime 
from django.http import JsonResponse
import requests

from livros.models import *
from livros.serializers import *
from .filters import *
from core.models import User
from core.permissions import IsBibliotecario, IsAdministradores, IsUsuarios
from rest_framework.decorators import api_view

class CategoriaViewSet(ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, IsBibliotecario]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_categoria',)

    def list(self, request, *args, **kwargs):
        categorias = []
        response_categoria_list_ifrn = requests.get('http://127.0.0.1:8001/api/categoria/')
        response_categoria_list_uern = requests.get('http://127.0.0.1:8002/api/categoria/')
        response_categoria_list_ufersa = requests.get('http://127.0.0.1:8003/api/categoria/')

        for categoria in response_categoria_list_ifrn.json():
            if not categoria['nome_categoria'] == '':
                categorias.append(categoria)
        for categoria in response_categoria_list_uern.json():
            if not categoria['nome_categoria'] == '':
                categorias.append(categoria)
        for categoria in response_categoria_list_ufersa.json():
            if not categoria['nome_categoria'] == '':
                categorias.append(categoria)
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        for categoria in serializer.data:
            if not categoria['nome_categoria'] == '':
                categorias.append(categoria)

        return Response(categorias)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filterset_class = EditoraFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_editora',)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        editoras = []
        response_editora_list_ifrn = requests.get('http://127.0.0.1:8001/api/editora/')
        response_editora_list_uern = requests.get('http://127.0.0.1:8002/api/editora/')
        response_editora_list_ufersa = requests.get('http://127.0.0.1:8003/api/editora/')

        for editora in response_editora_list_ifrn.json():
            if not editora['nome_editora'] == '':
                editoras.append(editora)
        for editora in response_editora_list_uern.json():
            if not editora['nome_editora'] == '':
                editoras.append(editora)
        for editora in response_editora_list_ufersa.json():
            if not editora['nome_editora'] == '':
                editoras.append(editora)
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        for editora in serializer.data:
            if not editora['nome_editora'] == '':
                editoras.append(editora)

        return Response(editoras)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_autor',)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class LivroViewSet(ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
    filterset_class = LivroFilter
    filter_backends = (SearchFilter,)
    search_fields = ('nome_livro',)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        livros = []
        response_livro_list_ifrn = requests.get('http://127.0.0.1:8001/api/livro/')
        response_livro_list_uern = requests.get('http://127.0.0.1:8002/api/livro/')
        response_livro_list_ufersa = requests.get('http://127.0.0.1:8003/api/livro/')
        
        for livro in response_livro_list_ifrn.json():
            livros.append(livro)
        for livro in response_livro_list_uern.json():
            livros.append(livro)
        for livro in response_livro_list_ufersa.json():
            livros.append(livro)
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        for livro in serializer.data:
            livros.append(livro)

        return Response(livros)
    
    def retrieve(self, request: Request, pk: int, *args, **kwargs):
        instituicao = request.query_params.get("instituicao")

        if instituicao == "IFRN":
            response_livro_list_ufersa = requests.get(f'http://127.0.0.1:8001/api/livro/{pk}/')
            return Response(response_livro_list_ufersa.json())
        
        if instituicao == "UERN":
            response_livro_list_ufersa = requests.get(f'http://127.0.0.1:8002/api/livro/{pk}/')
            return Response(response_livro_list_ufersa.json())
        
        if instituicao == "UFERSA":
            response_livro_list_ufersa = requests.get(f'http://127.0.0.1:8003/api/livro/{pk}/')
            return Response(response_livro_list_ufersa.json())

        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmprestimoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer
    filter_class = EmprestimoFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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

    
    
    
   
@api_view(['GET'])
def search_books(request):
    query = request.query_params.get('query', '')
    if not query:
        return Response({'error': 'Query parameter is required'}, status=400)

    #API do Project Gutenberg
    url = f'http://gutendex.com/books/?search={query}'
    response = requests.get(url)

    if response.status_code != 200:
        return Response({'error': 'Failed to fetch data from Gutenberg API'}, status=500)

    data = response.json()
    return Response(data)


# Funçãopara buscar livros na API do Project Gutenberg
def buscar_livros_gutendex(query):
    url = f'http://gutendex.com/books/?search={query}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao acessar a API do Project Gutenberg: {response.status_code}")
        return []

    data = response.json().get('results', [])
    resultados = []
    for item in data:
        resultados.append({
            'nome_livro': item.get('title'),
            'autor': ', '.join([author['name'] for author in item.get('authors', [{'name': 'Desconhecido'}])]),
            'editora': 'Project Gutenberg',
            'categoria': ', '.join(item.get('bookshelves', ['Desconhecida'])),
            'local': 'Gutenberg',
            'formatos': item.get('formats', {}),
            'download_count': item.get('download_count', 0),
        })

    #print(f"Resultados da API Gutenberg: {resultados}")
    return resultados



# Função principal para buscar livros
@api_view(['GET'])
def buscar_livro(request):
    query = request.GET.get('query', '')
    tipo = request.GET.get('tipo', 'nome_livro')

    if not query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)

    resultados = []

    # Pesquisa nos registros locais
    if tipo == 'nome_livro':
        livros_locais = Livro.objects.filter(nome_livro__icontains=query)
    elif tipo == 'autor':
        livros_locais = Livro.objects.filter(autor__nome_autor__icontains=query)
    elif tipo == 'categoria':
        livros_locais = Livro.objects.filter(categoria__nome_categoria__icontains=query)
    elif tipo == 'editora':
        livros_locais = Livro.objects.filter(editora__nome_editora__icontains=query)
    else:
        livros_locais = Livro.objects.none()

    for livro in livros_locais:
        resultados.append({
            'nome_livro': livro.nome_livro,
            'autor': livro.autor.nome_autor,
            'editora': livro.editora.nome_editora,
            'categoria': livro.categoria.nome_categoria,
            'local': 'Local'
        })

    print(f"Resultados locais: {resultados}")

    # API do Project Gutenbex
    resultados_gutendex = buscar_livros_gutendex(query)
    resultados.extend(resultados_gutendex)

    # URL das APIs externas
    urls_apis_externas = [
        'http://localhost:8001/api/livro/', #IFRN
        'http://localhost:8002/api/livro/', #UERN 
        'http://localhost:8003/api/livro/', #UFERSA
        
    ]

    
    def consumir_api_externa(url, params):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro na resposta da API {url}: {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API {url}: {e}")
            return []

    # Pesquisa nas APIs externas.
    for url in urls_apis_externas:
        dados_api = consumir_api_externa(url, {tipo: query})
        for item in dados_api:
            if query.lower() in item.get(tipo, '').lower():  # Verifica se o resultado contém a query
                resultados.append({
                    'nome_livro': item.get('nome_livro'),
                    'autor': item.get('autor'),
                    'editora': item.get('editora'),
                    'categoria': item.get('categoria'),
                    'local': url
                })

    print(f"Resultados finais: {resultados}")

    return JsonResponse(resultados, safe=False)
