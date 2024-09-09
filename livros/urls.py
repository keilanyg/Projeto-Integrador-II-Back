from django.urls import include, path
from rest_framework import routers

from livros.viewsets import *

router = routers.DefaultRouter()
app_name = "livros"
router.register("categoria", CategoriaViewSet)
router.register("editora", EditoraViewSet)
router.register("autor", AutorViewSet)
router.register("livro", LivroViewSet)
router.register("emprestimo", EmprestimoViewSet)
router.register("devolucao", DevolucaoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("buscar_livro/", buscar_livro, name="buscar_livro"),
    path("search/", search_books, name="search_books"),
    path("buscar-livro/", buscar_livro, name="buscar-livro"),
]
