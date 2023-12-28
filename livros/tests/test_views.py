from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from livros.tests.factories.test_factories import CategoriaFactory, EditoraFactory, AutorFactory, LivroFactory

class TestCategoriaModel(TestCase):
    
    def setUp(self):
        self.categoria = CategoriaFactory()

    def test_str_categoria(self):
        # Testar uma categoria como string
        self.assertEqual(str(self.categoria), self.categoria.nome_categoria)
        
class TestEditoraModel(TestCase):
    def setUp(self):
        self.editora = EditoraFactory()

    def test_str_editora(self):
        # Testar uma editora como string
        self.assertEqual(str(self.editora), self.editora.nome_editora)
        
class TestAutorModel(TestCase):
    def setUp(self):
        self.autor = AutorFactory()

    def test_str_autor(self):
        # Testar um autor como string
        self.assertEqual(str(self.autor), self.autor.nome_autor)


    