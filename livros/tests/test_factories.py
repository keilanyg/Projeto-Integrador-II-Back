from django.test import TestCase
from .factories import CategoriaFactory, AutorFactory, LivroFactory, EditoraFactory
from livros.models import Categoria, Autor, Livro, Editora

class CategoriaTestCase(TestCase):
    def test_livro_creation(self):
        autor = AutorFactory
        livro = LivroFactory(autor = autor)
        
        #verificando a criação
        self.assertIsInstance(autor, Autor)
        self.assertIsInstance(livro, Livro)
        
