from django.contrib import admin
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo

admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Emprestimo)