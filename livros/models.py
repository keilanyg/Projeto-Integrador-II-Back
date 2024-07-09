from django.db import models
from core.models import User


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.nome_categoria


class Editora(models.Model):
    nome_editora = models.CharField(max_length=250, verbose_name="Editora")

    def __str__(self):
        return self.nome_editora


class Autor(models.Model):
    class Meta: 
        verbose_name_plural = "Autores"

    nome_autor = models.CharField(max_length=250, verbose_name="Autor")

    def __str__(self):
        return self.nome_autor


class Livro(models.Model):
    nome_livro = models.CharField(max_length=100, verbose_name="Nome do Livro")
    data_cadastro = models.DateField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    descricao_livro = models.TextField(max_length=200, verbose_name="Descrição do Livro", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    cover = models.ImageField(upload_to='livros/cover/%Y/%m/%d/')

    def __str__(self):
        return self.nome_livro


class Emprestimo(models.Model):
    nome_emprestado_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário Cadastrado")
    data_emprestimo = models.DateField(verbose_name="Data de Empréstimo", auto_now_add=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")

    def __str__(self):
        return f"LIVRO: {self.livro} - USUÁRIO: {self.nome_emprestado_usuario}"


def verificar_livros_emprestados():
    total_livros = Livro.objects.count()
    livros_emprestados = Emprestimo.objects.count()
    return livros_emprestados

# Remover chamadas de funções fora de contexto apropriado


class Devolucao(models.Model):
    emprestimo = models.OneToOneField('livros.Emprestimo', on_delete=models.CASCADE, verbose_name="Livro")
    usuario_devolucao = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário de Devolução")
    data_devolucao = models.DateField(verbose_name="Data de Devolução")

    def __str__(self):
        return f"Devolução {self.emprestimo}"
