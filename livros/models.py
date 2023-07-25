from django.db import models
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import request
from core.models import User
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdministradores, IsBibliotecario, IsUsuarios


class Categoria(models.Model):
    #permission_class = [IsAuthenticated & (IsBibliotecario)]
    nome_categoria = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.nome_categoria

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

 
class Editora(models.Model):
    nome_editora = models.CharField(max_length=250, verbose_name="Editora")

    def __str__(self):
        return self.nome_editora
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

class Autor(models.Model):
    
    class Meta: 
        verbose_name_plural = "Autores"
    
    nome_autor = models.CharField(max_length=250, verbose_name="Autor")

    def __str__(self):
        return self.nome_autor
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class Livro(models.Model):
    nome_livro = models.CharField(max_length = 100, verbose_name="Nome do Livro")
    data_cadastro = models.DateField(auto_now_add= True, verbose_name="Data de Cadastro")
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    descricao_livro = models.TextField(max_length=200, verbose_name="Descrição do Livro", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    cover = models.ImageField() #campo para receber imagem que vai colocar dentro da pasta livros/cover junto com o ano, mês e dia
    
    def __str__(self):
        return self.nome_livro
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    
    

"""@permission_required('livros.adicionar_emprestimo') """  
class Emprestimo(models.Model):
    nome_emprestado_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário Cadastrado")
    data_emprestimo = models.DateField(verbose_name="Data de Empréstimo", auto_now_add=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    
    
    #alerta_devolucao = models.BooleanField(default=False)
    
    def __str__(self):
        return str(f"LIVRO: {self.livro} - USUÁRIO: {self.nome_emprestado_usuario}")
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def quantidade_emprestado(self):
        obj =(Livro.objects.filter)
        quant = self.livro.quantidade
        num_emprestado = quant -1
        num_disponivel = quant - num_emprestado
        return("Quantidade de livros emprestados", num_emprestado, " Quantidade disponivel ", num_disponivel)
 
def verificar_livros_emprestados():
        
    total_livros = Livro.objects.count()
    livros_emprestados = Emprestimo.objects.count()

    return livros_emprestados

# Chamada da função para obter o número de livros emprestados
livros_emprestados = verificar_livros_emprestados()

print(f"Total de livros emprestados: {livros_emprestados}")

class Devolucao(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    emprestimo = models.OneToOneField('livros.Emprestimo', on_delete=models.CASCADE, verbose_name="Livro")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    #usuario_devolucao = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário de Devolução")
    data_devolucao = models.DateField(verbose_name="Data de Devolução")
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self):
        return f"Devolução {self.emprestimo}"

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    
