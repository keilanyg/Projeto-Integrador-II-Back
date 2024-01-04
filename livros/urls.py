from django.urls import path, include
from livros.viewsets import categoria, editora, autor, livro, emprestimo, devolucao
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'livros'
router.register("categoria", categoria)
router.register("editora", editora)
router.register("autor", autor)
router.register("livro", livro)
router.register("emprestimo", emprestimo)
router.register("devolucao", devolucao)

urlpatterns = [
    path("", include(router.urls)),
]
