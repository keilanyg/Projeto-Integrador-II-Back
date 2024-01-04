from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from livros.models import Categoria, Editora, Autor, Livro

        
from django.test import TestCase
from django.urls import reverse  # Se você ainda precisar importar reverse
from rest_framework import status
from rest_framework.test import APIClient
from livros.models import Categoria, Editora, Autor, Livro

class CategoriaAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.categoria = Categoria.objects.create(nome_categoria='Test Categoria')

    def test_get_categorias_list(self):
        url = '/api/categoria/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_categoria_detail(self):
        url = f'/api/categoria/{self.categoria.id}/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_categoria_object(self):
        url = f'/api/categoria/{self.categoria.id}/'  
        print(f"URL para DELETE: {url}")  
        response = self.client.delete(url)
        print(f"Status Code: {response.status_code}")  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Categoria.DoesNotExist):
            Categoria.objects.get(id=self.categoria.id)


# Restante do código permanece inalterado


class EditoraAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.editora = Editora.objects.create(nome_editora='Test Editora')

    def test_get_editoras_list(self):
        url = '/api/editora'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_editora_detail(self):
        url = f'/api/editora/{self.editora.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_editora_object(self):
        url = f'/api/editora/{self.editora.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Editora.DoesNotExist):
            Editora.objects.get(id=self.editora.id)
    

class AutorAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.autor = Autor.objects.create(nome_autor='Test Autor')

    def test_get_autores_list(self):
        url = '/api/autor/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_autor_detail(self):
        url = f'/api/autor/{self.autor.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_autor_object(self):
        url = f'/api/autor/{self.autor.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Autor.DoesNotExist):
            Autor.objects.get(id=self.autor.id)
        

class LivroAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.categoria = Categoria.objects.create(nome_categoria='Test Categoria')
        self.editora = Editora.objects.create(nome_editora='Test Editora')
        self.autor = Autor.objects.create(nome_autor='Test Autor')
        self.livro = Livro.objects.create(
            nome_livro='Test Book',
            data_cadastro='2022-01-01',
            data_lancamento='2022-01-01',
            quantidade=10,
            descricao_livro='Test Descrição',
            categoria=self.categoria,
            editora=self.editora,
            autor=self.autor,
            cover='path/to/cover.jpg',
        )

    def test_get_livros_list(self):
        url = '/api/livro/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_livro_detail(self):
        url = f'/api/livro/{self.livro.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_livro_object(self):
        url = f'/api/livro/{self.livro.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the object is deleted from the database
        with self.assertRaises(Livro.DoesNotExist):
            Livro.objects.get(id=self.livro.id)