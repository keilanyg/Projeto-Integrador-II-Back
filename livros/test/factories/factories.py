import factory
from factory import Faker

from livros.models import Categoria, Editora, Autor, Livro

class CategoriaFactory(factory.Factory):
    class Meta:
        model = Categoria

    nome_categoria = factory.Faker('word')

class EditoraFactory(factory.Factory):
    class Meta:
        model = Editora
    
    nome_editora = factory.Faker('word')  

class LivroFactory(factory.Factory):
    class Meta:
        model = Livro

    nome_livro = factory.Faker('sentence', nb_words=3)
    data_cadastro = factory.Faker('date_this_decade')
    data_lancamento = factory.Faker('date_this_decade')
    quantidade = factory.Faker("random_digit_not_null")
    descricao_livro = factory.Faker('paragraph', nb_sentences=3)
    categoria = factory.SubFactory(CategoriaFactory)
    editora = factory.SubFactory(EditoraFactory)  
    autor = factory.Faker('name')  
    cover = factory.Faker('url')

class AutorFactory(factory.Factory):
    class Meta:
        model = Autor
    
    nome_autor = factory.Faker('word')  
