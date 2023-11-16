import factory
from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger

from livros.models import Categoria, Editora, Autor, Livro

class CategoriaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Categoria
        name = Faker('name')

class EditoraFactory(factory.DjangoModelFactory):
    class Meta:
        model = Editora
        name = Faker('name')
                
class LivroFactory(factory.DjangoModelFactory):
    class Meta:
        model = Livro
        name = Faker('name')

class AutorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Autor
        name = Faker('name')
        

