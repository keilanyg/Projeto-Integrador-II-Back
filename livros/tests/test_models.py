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
        self.editora = Categoria.objects.create(nome='Tecnologia')


class AutorModelTest(TestCase):
    pass

class LivroModelTest(TestCase):
    pass

class EmprestimoModelTest(TestCase):
    pass

class DevolucaoModelTest(TestCase):
    pass
