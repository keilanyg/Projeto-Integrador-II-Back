from django.test import TestCase
"""from ..models import Categoria
import datetime
from rest_framework import status
from django.urls import reverse"""
from livros.tests.factories.factories import CategoriaFactory

class TestCategoriaModel(TestCase):
    
    def setUp(self):
        categoria = CategoriaFactory()

    def test_str_categoria(self):
        # Testar a criação de uma categoria
        self.assertEqual(self.categoria.nome_categoria, self.categoria.__str__())
"""class EditoraModelTest(TestCase):
    
        pass

class AutorModelTest(TestCase):
    def setUp(self):
        # Criar categoria
        self.autor = Autor.objects.create(nome='Augusto')

    def test_criar_categoria(self):
        # Testar a criação de uma categoria
        data = {'nome_autor': 'Nicolas'}
        response = self.client.post(reverse('autor-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)
        self.assertEqual(Autor.objects.get(nome='Nicolas').nome, 'Nicolas')

    def test_obter_categoria(self):
        # Testar a obtenção de uma categoria
        response = self.client.get(reverse('autor-detail', args=[self.autor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Augusto')

    def test_listar_categorias(self):
        # Testar a listagem de categorias
        response = self.client.get(reverse('autor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Augusto')

class LivroModelTest(TestCase):
    pass

class EmprestimoModelTest(TestCase):
    pass

class DevolucaoModelTest(TestCase):
    pass
"""