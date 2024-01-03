from django.test import TestCase

from livros.serializers import AutorSerializer, LivrosSerializer, CategoriaSerializer, EditoraSerializer
from livros.models import Categoria, Editora, Autor

class AutorSerializerTest(TestCase):
    def test_serialize_autor(self):
        autor_data = {'nome_autor': 'Jane Doe'}
        serializer = AutorSerializer(data=autor_data)
        self.assertTrue(serializer.is_valid())
        autor_instance = serializer.save()
        self.assertEqual(str(autor_instance), 'Jane Doe')
        
class CategoriaSerializerTest(TestCase):
    def test_serialize_categoria(self):
        categoria_data = {'nome_categoria': 'Romance'}
        serializer = CategoriaSerializer(data=categoria_data)
        self.assertTrue(serializer.is_valid())
        categoria_instance = serializer.save()
        self.assertEqual(str(categoria_instance), 'Romance')
        
class EditoraSerializerTest(TestCase):
    def test_serialize_editora(self):
        editora_data = {'nome_editora': 'Inova'}
        serializer = EditoraSerializer(data=editora_data)
        self.assertTrue(serializer.is_valid())
        editora_instance = serializer.save()
        self.assertEqual(str(editora_instance), 'Inova')
        
"""class LivroSerializerTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome_categoria='Ficção')
        self.editora = Editora.objects.create(nome_editora='Editora ABC')
        self.autor = Autor.objects.create(nome_autor='John Doe')

    def test_serialize_livro(self):
        livro_data = {
            'nome_livro': 'A culpa e das estrelas',
            'data_cadastro': '2023-01-01',
            'data_lancamento': '2022-01-01',
            'quantidade': 1,
            'descricao_livro': 'livro de ficcao',
            'categoria': self.categoria.id,
            'editora': self.editora.id,
            'autor': self.autor.id,
            'cover': 'livros/cover/cover_image.jpg',
        }
        serializer = LivrosSerializer(data=livro_data)
        self.assertTrue(serializer.is_valid())
        livro_instance = serializer.save()
        self.assertEqual(str(livro_instance), 'A culpa e das estrelas')"""