from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Categoria")
    
    def __str__(self):
        return self.nome
    
    
class Editora(models.Model):
    nome = models.CharField(max_length=250, verbose_name="Editora")

    def __str__(self):
        return self.nome

class Autor(models.Model):
    class Meta: 
        verbose_name_plural = "Autores"
    
    nome = models.CharField(max_length=250, verbose_name="Nome")

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    autor = models.ForeignKey(Autor, on_delete= models.PROTECT, verbose_name="Autor")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria")
    datacadastro = models.DateField(verbose_name="Data de Cadastro")
    datalancamento = models.DateField(verbose_name="Data de Lançamento")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, verbose_name="Editora")
    quantidade = models.IntegerField(verbose_name="Quantidade")

    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    dataemprestimo = models.DateField(verbose_name="Data de Empréstimo")
    datadevolucao = models.DateField(verbose_name="Data de Devolução")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, verbose_name="Livro a ser emprestado")
