from django.test import TestCase
from ...viewsets import categoria, autor, livro, devolucao, emprestimo

class GenericViewTest(TestCase):
    """Classe genérica para testar status code 200 de views."""

    def test_status_code_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class CategoriaViewTestCase(GenericViewTest):
    """Testes para a view de categoria."""
    url = '/api/categoria'

class AutorViewTestCase(GenericViewTest):
    """Testes para a view de autor."""
    url = '/api/autor'

class LivroViewTestCase(GenericViewTest):
    """Testes para a view de livro."""
    url = '/api/livro'

class EmprestimoViewTestCase(GenericViewTest):
    """Testes para a view de emprestimo."""
    url = '/api/emprestimo'

class DevolucaoViewTestCase(GenericViewTest):
    """Testes para a view de devolucao."""
    url = '/api/devolucao'
