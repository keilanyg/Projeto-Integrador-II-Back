from django.test import TestCase
"""from ..models import Categoria
import datetime
from rest_framework import status
from django.urls import reverse"""
from livros.tests.factories.factories import CategoriaFactory, EditoraFactory, AutorFactory, LivroFactory

class TestCategoriaModel(TestCase):
    
    def setUp(self):
        self.categoria = CategoriaFactory()

    def test_str_categoria(self):
        # Testar a criação de uma categoria
        self.assertEqual(self.categoria.nome_categoria, self.categoria.__str__())

class EditoraModelTest(TestCase):
    def setUp(self):
        self.editora = EditoraFactory()

    def test_str_categoria(self):
        # Testar a criação de uma editora
        self.assertEqual(self.editora.nome_editora, self.editora.__str__())


class AutorModelTest(TestCase):
    def setUp(self):
        # Criar autor
        self.autor = Autor.objects.create(nome='Augusto')

    def test_criar_autor(self):
        # Testar a criação de um autor
        data = {'nome_autor': 'Nicolas'}
        response = self.client.post(reverse('autor-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)
        self.assertEqual(Autor.objects.get(nome='Nicolas').nome, 'Nicolas')

    def test_obter_autor(self):
        # Testar a obtenção de um autor
        response = self.client.get(reverse('autor-detail', args=[self.autor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Augusto')

    def test_listar_autores(self):
        # Testar a listagem de autores
        response = self.client.get(reverse('autor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Augusto')

class LivroModelTest(TestCase):
    
    def test_criar_livro(self):
        livro = LivroFactory()
        self.assertEqual(Livro.objects.count(), 1)
        self.assertEqual(Livro.objects.get(), livro)


class EmprestimoModelTest(TestCase):

    def test_criar_emprestimo(self):
        livro = LivroFactory()
        emprestimo = Emprestimo.objects.create(livro=livro)
        self.assertEqual(Emprestimo.objects.count(), 1)
        self.assertEqual(Emprestimo.objects.get(), emprestimo)

class DevolucaoModelTest(TestCase):

    def test_criar_devolucao(self):
        livro = LivroFactory()
        emprestimo = Emprestimo.objects.create(livro=livro)
        devolucao = Devolucao.objects.create(emprestimo=emprestimo)
        self.assertEqual(Devolucao.objects.count(), 1)
        self.assertEqual(Devolucao.objects.get(), devolucao)
