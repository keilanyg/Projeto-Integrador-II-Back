from django.urls import path, include
from livros.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'livros'
router.register("categoria", CategoriaViewSet)
router.register("editora", EditoraViewSet)
router.register("autor", AutorViewSet)
router.register("livro", LivroViewSet)
router.register("emprestimo", EmprestimoViewSet)
router.register("devolucao", DevolucaoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
