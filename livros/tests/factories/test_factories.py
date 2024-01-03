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
     
class LivroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Livro

    nome_livro = factory.Faker('sentence', nb_words=3)
    data_cadastro = factory.Faker('date')
    data_lancamento = factory.Faker('date')
    quantidade = factory.Faker('random_int', min=1, max=100)
    descricao_livro = factory.Faker('paragraph')
    categoria = factory.SubFactory(CategoriaFactory)  # Substitua pelo nome real da fábrica CategoriaFactory
    editora = factory.SubFactory(EditoraFactory)  # Substitua pelo nome real da fábrica EditoraFactory
    autor = factory.SubFactory(AutorFactory)  # Substitua pelo nome real da fábrica AutorFactory
    cover = factory.Faker('image_url')