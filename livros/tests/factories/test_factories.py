"""from django.test import TestCase
from .factories import AutorFactory, LivroFactory
from livros.models import Autor, Livro

class CategoriaTestCase(TestCase):
    def test_livro_creation(self):
        autor = AutorFactory
        livro = LivroFactory(autor = autor)
        
        #verificando a criação
        self.assertIsInstance(autor, Autor)
        self.assertIsInstance(livro, Livro)
        
"""