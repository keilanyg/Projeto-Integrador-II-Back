from rest_framework import generics
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo
from livros.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivrosSerializer, EmprestimosSerializer

# GET E POST
class categorialist(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# GET, PUT E DELETE -> (ID)              
class detalhe_categoria(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer  

# GET E POST
class editoralist(generics.ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

# GET, PUT E DELETE -> (ID)   
class detalhe_editora(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

# GET E POST 
class autorlist(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
 
# GET, PUT E DELETE -> (ID) 
class detalhe_autor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# GET E POST 
class livrolist(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer

# GET, PUT E DELETE -> (ID) 
class detalhe_livro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer

# GET E POST 
class emprestimolist(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer

# GET, PUT E DELETE -> (ID) 
class detalhe_emprestimo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializer

 