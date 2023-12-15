from django.test import TestCase
from .factories import AutorFactory, LivroFactory, EditoraFactory
from livros.models import Autor, Livro, Editora, Categoria

class CategoriaTestCase(TestCase):
    def test_livro_creation(self):
        autor = AutorFactory
        livro = LivroFactory(autor = autor)
        
        #verificando a criação
        self.assertIsInstance(autor, Autor)
        self.assertIsInstance(livro, Livro)
        
class EditoraTestCase(TestCase):
    def test_editora_creation(self):
        editora = EditoraFactory()
        #verificando a criação
        self.assertIsInstance(editora, Editora)
        