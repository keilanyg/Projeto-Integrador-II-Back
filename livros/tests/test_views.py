from django.test import TestCase
from ..viewsets import categoria, autor, livro, devolucao, emprestimo

class categoriaViewTesteCase(TestCase):
    
    def test_status_code_200(self):
        response = self.client.get('/api/categoria')
        self.assertEqual(response.status_code, 200)

class autorViewTesteCase(TestCase):
    
    def test_status_code_200(self):
        response = self.client.get('/api/autor')
        self.assertEqual(response.status_code, 200)
        
        
class livroViewTesteCase(TestCase):
    
    def test_status_code_200(self):
        response = self.client.get('/api/livro')
        self.assertEqual(response.status_code, 200)
        
class emprestimoViewTesteCase(TestCase):
    
    def test_status_code_200(self):
        response = self.client.get('/api/emprestimo')
        self.assertEqual(response.status_code, 200)
        
class devolucaoViewTesteCase(TestCase):
    
    def test_status_code_200(self):
        response = self.client.get('/api/devolucao')
        self.assertEqual(response.status_code, 200)