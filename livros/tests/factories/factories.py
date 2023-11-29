import factory
from factory import Faker
"""from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger"""

from livros.models import Categoria

class CategoriaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Categoria
        nome_categoria = Faker('name')

"""class EditoraFactory(factory.DjangoModelFactory):
    class Meta:
        model = Editora
        nome_autor = Faker('name')
                
class LivroFactory(factory.DjangoModelFactory):
    class Meta:
        model = Livro
        nome_livro = Faker('name')
        data_cadastro = Faker
        data_lancamento = Faker
        quantidade = Faker("numerify")
        descricao_livro = Faker("")
        categoria = factory.SubFactory(CategoriaFactory.id)
        editora = factory.SubFactory(EditoraFactory.id)
        autor = Faker("")
        cover = Faker("")

class AutorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Autor
        name = Faker('name')"""
        

