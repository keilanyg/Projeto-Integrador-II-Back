from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from livros.models import Categoria

class CategoriaAPITestCase(TestCase):

    def setUp(self):
        #categoria de teste
        self.categoria = Categoria.objects.create(nome_categoria='Categoria Teste')
        self.client = APIClient()

    def test_listar_categorias(self):
        url = 'http://localhost:8000/api/categoria/'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Categoria Teste')
        
    def test_detalhes_categoria(self):
        url = f'http://localhost:8000/api/categoria/{self.categoria.pk}/'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Categoria Teste')

    def test_criar_categoria_autenticado(self):
        url = 'http://localhost:8000/api/categoria/'  
        data = {'nome_categoria': 'Nova Categoria'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.count(), 2)

    def test_atualizar_categoria_autenticado(self):
        url = f'http://localhost:8000/api/categoria/{self.categoria.pk}/'  
        data = {'nome_categoria': 'Categoria Atualizada'}

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Categoria.objects.get(pk=self.categoria.pk).nome_categoria, 'Categoria Atualizada')

    def test_excluir_categoria_autenticado(self):
        url = f'http://localhost:8000/api/categoria/{self.categoria.pk}/'  

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Categoria.objects.count(), 0)