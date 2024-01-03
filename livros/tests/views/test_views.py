from django.test import TestCase, Client
from django.urls import reverse

class test_minhas_views(TestCase):
    def test_minha_view_categoria(self):
        response = self.client.get('http://localhost:8000/api/categoria/')
        self.assertEqual(response.status_code, 200)
       
    def test_minha_view_editora(self):
        response = self.client.get('http://localhost:8000/api/editora/')
        self.assertEqual(response.status_code, 200)
        
    def test_minha_view_autor(self):
        response = self.client.get('http://localhost:8000/api/autor/')
        self.assertEqual(response.status_code, 200)
        
    def test_minha_view_livro(self):
        response = self.client.get('http://localhost:8000/api/livro/')
        self.assertEqual(response.status_code, 200) 
        
    def test_minha_view_emprestimo(self):
        response = self.client.get('http://localhost:8000/api/emprestimo/')
        self.assertEqual(response.status_code, 200) 
        
    def test_minha_view_devolucao(self):
        response = self.client.get('http://localhost:8000/api/devolucao/')
        self.assertEqual(response.status_code, 200) 
        
    