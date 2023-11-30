import factory
from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger

from livros.models import Categoria, Editora, Autor, Livro

class CategoriaFactory(factory.Factory):
    class Meta:
        model = Categoria

    nome_categoria = factory.Faker('word')

class EditoraFactory(factory.Factory):

    class Meta:
        model = Editora
    
    nome_editora = Faker('Edson')
                
class LivroFactory(factory.Factory):

    class Meta:
        model = Livro

    nome_livro = Faker('sentence', nb_words=3)
    data_cadastro = Faker('date_this_decade')
    data_lancamento = Faker('date_this_decade')
    quantidade = Faker("random_digit_not_null")
    descricao_livro = Faker('paragraph', nb_sentences=3)
    categoria = factory.SubFactory(CategoriaFactory)
    nome_editora = factory.SubFactory(EditoraFactory)
    nome_autor = Faker('name')
    cover = Faker('url')

class AutorFactory(factory.Factory):

    class Meta:
        model = Autor
    
    nome_autor = Faker('Fernando')
        

