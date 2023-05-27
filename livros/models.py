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
    
    nome = models.CharField(max_length=250, verbose_name="Autor")

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length = 100)
    data_cadastro = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    nome_emprestado = models.CharField(max_length=255, verbose_name="Nome")
    dataemprestimo = models.DateField(verbose_name="Data de Empréstimo")
    datadevolucao = models.DateField(verbose_name="Data de Devolução")
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self):
        return f"{self.nome_emprestado}"