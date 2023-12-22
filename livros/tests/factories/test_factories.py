import factory
from factory import Faker
from factory.django import DjangoModelFactory

from livros.models import Categoria, Editora, Autor, Livro

class CategoriaFactory(factory.Factory):
    class Meta:
        model = Categoria

    nome_categoria = factory.Faker('word')

class EditoraFactory(factory.Factory):
    class Meta:
        model = Editora
    
    nome_editora = factory.Faker('company')  
    
class AutorFactory(factory.Factory):
    class Meta:
        model = Autor
    
    nome_autor = factory.Faker('name') 
     
class LivroFactory(DjangoModelFactory):
    class Meta:
        model = Livro

    nome_livro = factory.Faker('sentence')
    data_cadastro = factory.Faker('date_this_decade')
    data_lancamento = factory.Faker('date_this_decade')
    quantidade = factory.Faker('random_int', min=1, max=100)
    descricao_livro = factory.Faker('paragraph')
    categoria = factory.SubFactory(CategoriaFactory)
    editora = factory.SubFactory(EditoraFactory)
    autor = factory.SubFactory(AutorFactory)
    cover = factory.django.ImageField()