from django.test import TestCase
from ..models import Categoria, Editora, Livro, Autor, Emprestimo, Devolucao
import datetime
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class CategoriaTestCase(TestCase):
    
    def setUp(self):
        # Criar categoria
        self.categoria = Categoria.objects.create(nome='Tecnologia')

    def test_criar_categoria(self):
        # Testar a criação de uma categoria
        data = {'nome_categoria': 'Automobilismo'}
        response = self.client.post(reverse('categoria-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.count(), 2)
        self.assertEqual(Categoria.objects.get(nome='Automobilismo').nome, 'Automobilismo')

    def test_obter_categoria(self):
        # Testar a obtenção de uma categoria
        response = self.client.get(reverse('categoria-detail', args=[self.categoria.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Tecnologia')

    def test_listar_categorias(self):
        # Testar a listagem de categorias
        response = self.client.get(reverse('categoria-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Tecnologia')

    
    """"def test_categoria(self):
        teste = Categoria.objects.create(nome_categoria='romance')
    
"""

class EditoraModelTest(TestCase):
    def setUp(self):
        # Criar categoria
        self.categoria = Categoria.objects.create(nome='Tecnologia')
        # Criar editora
        self.editora = Editora.objects.create(nome='Livraria ABC')

    def test_criar_editora(self):
        # Testar a criação de uma editora
        data = {'nome': 'Livraria XYZ'}
        response = self.client.post(reverse('editora-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Editora.objects.count(), 2)
        self.assertEqual(Editora.objects.get(nome='Livraria XYZ').nome, 'Livraria XYZ')

    def test_obter_editora(self):
        # Testar a obtenção de uma editora
        response = self.client.get(reverse('editora-detail', args=[self.editora.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Livraria XYZ')

    def test_listar_editoras(self):
        # Testar a listagem de editoras
        response = self.client.get(reverse('editora-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Livraria XYZ')

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
