from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from livros.models import Autor, Livro, Emprestimo, Devolucao  # Certifique-se de importar os modelos necessários
from livros.test.factories.factories import CategoriaFactory, EditoraFactory, AutorFactory, LivroFactory

class TestCategoriaModel(TestCase):
    
    def setUp(self):
        self.categoria = CategoriaFactory()

    def test_str_categoria(self):
        # Testar a representação de uma categoria como string
        self.assertEqual(str(self.categoria), self.categoria.nome_categoria)

class EditoraModelTest(TestCase):
    def setUp(self):
        self.editora = EditoraFactory()

    def test_str_editora(self):
        # Testar a representação de uma editora como string
        self.assertEqual(str(self.editora), self.editora.nome_editora)

class AutorModelTest(TestCase):
    def setUp(self):
        # Criar autor usando a factory
        self.autor = AutorFactory()

    def test_criar_autor(self):
        # Testar a criação de um autor via POST
        data = {'nome_autor': 'Nicolas'}
        response = self.client.post(reverse('autor-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)
        self.assertEqual(Autor.objects.get(nome='Nicolas').nome, 'Nicolas')

    def test_obter_autor(self):
        # Testar a obtenção de um autor via GET
        response = self.client.get(reverse('autor-detail', args=[self.autor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_autor'], self.autor.nome_autor)

    def test_listar_autores(self):
        # Testar a listagem de autores
        response = self.client.get(reverse('autor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome_autor'], self.autor.nome_autor)

class LivroModelTest(TestCase):
    
    def test_criar_livro(self):
        livro = LivroFactory()
        self.assertEqual(Livro.objects.count(), 1)
        self.assertEqual(str(Livro.objects.get()), str(livro))

class EmprestimoModelTest(TestCase):

    def test_criar_emprestimo(self):
        livro = LivroFactory()
        emprestimo = Emprestimo.objects.create(livro=livro)
        self.assertEqual(Emprestimo.objects.count(), 1)
        self.assertEqual(str(Emprestimo.objects.get()), str(emprestimo))

class DevolucaoModelTest(TestCase):

    def test_criar_devolucao(self):
        livro = LivroFactory()
        emprestimo = Emprestimo.objects.create(livro=livro)
        devolucao = Devolucao.objects.create(emprestimo=emprestimo)
        self.assertEqual(Devolucao.objects.count(), 1)
        self.assertEqual(str(Devolucao.objects.get()), str(devolucao))
