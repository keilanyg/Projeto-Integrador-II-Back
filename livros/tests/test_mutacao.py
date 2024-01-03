from django.test import TestCase
from .factories.test_factories import CategoriaFactory, AutorFactory, EditoraFactory, LivroFactory
import graphene
from graphene_django.types import DjangoObjectType
from livros.models import Livro

class TestCategoriaModelMut(TestCase):
    def setUp(self):
        self.categoria = CategoriaFactory()

    def test_str_categoria(self):
        mutated_categoria = self.categoria
        mutated_categoria.nome_categoria = "Nome Categoria Mutado"
        self.assertEqual(str(mutated_categoria), "Nome Categoria Mutado")

class TestAutorModelMut(TestCase):
    def setUp(self):
        self.autor = AutorFactory()

    def test_str_autor(self):
        mutated_autor = self.autor
        mutated_autor.nome_autor = "Nome Autor Mutado"
        self.assertEqual(str(mutated_autor), "Nome Autor Mutado")

class TestEditoraModelMut(TestCase):
    def setUp(self):
        self.editora = EditoraFactory()

    def test_str_editora(self):
        mutated_editora = self.editora
        mutated_editora.nome_editora = "Nome Editora Mutado"
        self.assertEqual(str(mutated_editora), "Nome Editora Mutado")
        

class LivroType(DjangoObjectType):
    class Meta:
        model = Livro

class MutateLivro(graphene.Mutation):
    class Arguments:
        livro_id = graphene.Int(required=True)
        nova_descricao = graphene.String(required=True)

    livro = graphene.Field(LivroType)

    def mutate(self, info, livro_id, nova_descricao):
        livro = Livro.objects.get(pk=livro_id)
        livro.descricao_livro = nova_descricao
        livro.save()

        return MutateLivro(livro=livro)

class Mutation(graphene.ObjectType):
    mutate_livro = MutateLivro.Field()