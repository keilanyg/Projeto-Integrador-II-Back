from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from livros.models import Editora

class EditoraAPITestCase(TestCase):

    def setUp(self):
        #Editora de teste
        self.Editora = Editora.objects.create(nome_editora='Editora Teste')
        self.client = APIClient()

    def test_listar_Editoras(self):
        url = 'http://localhost:8000/api/editora/'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Editora Teste')
        
    def test_detalhes_Editora(self):
        url = f'http://localhost:8000/api/editora/{self.Editora.pk}/'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Editora Teste')

    def test_criar_Editora_autenticado(self):
        url = 'http://localhost:8000/api/editora/'  
        data = {'nome_editora': 'Nova Editora'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Editora.objects.count(), 2)

    def test_atualizar_Editora_autenticado(self):
        url = f'http://localhost:8000/api/editora/{self.Editora.pk}/'  
        data = {'nome_editora': 'Editora Atualizada'}

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Editora.objects.get(pk=self.Editora.pk).nome_editora, 'Editora Atualizada')

    def test_excluir_Editora_autenticado(self):
        url = f'http://localhost:8000/api/editora/{self.Editora.pk}/'  

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Editora.objects.count(), 0)