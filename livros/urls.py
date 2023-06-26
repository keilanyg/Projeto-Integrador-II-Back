from django.urls import path, include
from livros.viewsets import categoria, editora, autor, livro, emprestimo
from rest_framework import routers

router = routers.SimpleRouter()

router.register("categoria", categoria)
router.register("editora", editora)
router.register("autor", autor)
router.register("livro", livro)
router.register("emprestimo", emprestimo)

urlpatterns = [
    path("", include(router.urls)),
]
