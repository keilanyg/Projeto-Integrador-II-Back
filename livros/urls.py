from django.urls import path
from livros.views import categorialist, detalhe_categoria, editoralist, detalhe_editora, autorlist, detalhe_autor, livrolist, detalhe_livro

urlpatterns = [
    path('categorialist', categorialist.as_view()),
    path('detalhe_categoria/<int:pk>',detalhe_categoria.as_view()),
    path('editoralist', editoralist.as_view()),
    path('detalhe_editora/<int:pk>', detalhe_editora.as_view()),
    path('autorlist', autorlist.as_view()),
    path('detalhe_autor/<int:pk>', detalhe_autor.as_view()),
    path('livrolist', livrolist.as_view()),
    path('detalhe_livro/<int:pk>', detalhe_livro.as_view()),
]