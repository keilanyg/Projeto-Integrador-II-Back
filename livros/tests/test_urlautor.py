from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from livros.models import Autor

class AutorAPITestCase(TestCase):

    def setUp(self):
        #Autor de teste
        self.Autor = Autor.objects.create(nome_autor='Autor Teste')
        self.client = APIClient()

    def test_listar_Autors(self):
        url = 'http://localhost:8000/api/autor/'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Autor Teste')
        
    def test_detalhes_Autor(self):
        url = f'http://localhost:8000/api/autor/{self.Autor.pk}/'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Autor Teste')

    def test_criar_Autor_autenticado(self):
        url = 'http://localhost:8000/api/autor/'  
        data = {'nome_autor': 'Nova Autor'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)

    def test_atualizar_Autor_autenticado(self):
        url = f'http://localhost:8000/api/autor/{self.Autor.pk}/'  
        data = {'nome_autor': 'Autor Atualizada'}

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Autor.objects.get(pk=self.Autor.pk).nome_autor, 'Autor Atualizada')

    def test_excluir_Autor_autenticado(self):
        url = f'http://localhost:8000/api/autor/{self.Autor.pk}/'  

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Autor.objects.count(), 0)