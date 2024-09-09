from rest_framework.routers import DefaultRouter
from django.urls import path
from core.viewsets import UserViewSet, UserProviderView
from livros.viewsets import (
    AutorViewSet,
    CategoriaViewSet,
    DevolucaoViewSet,
    EditoraViewSet,
    EmprestimoViewSet,
    LivroViewSet,
)

router = DefaultRouter()

router.register("user", UserViewSet)
router.register("categoria", CategoriaViewSet)
router.register("editora", EditoraViewSet)
router.register("autor", AutorViewSet)
router.register("livro", LivroViewSet)
router.register("emprestimo", EmprestimoViewSet)
router.register("devolucao", DevolucaoViewSet)

urlpatterns = [path("user/provider/", UserProviderView.as_view())] + router.urls
