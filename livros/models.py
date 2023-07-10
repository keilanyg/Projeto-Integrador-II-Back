from django.db import models
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name="Categoria")
    
    def __str__(self):
        return self.nome_categoria

    @method_decorator(permission_required('livros.adicionar_categoria'))
    def save(self, *args, **kwargs):
        # salvando informacoes no db
        super().save(*args, **kwargs)

 
class Editora(models.Model):
    nome_editora = models.CharField(max_length=250, verbose_name="Editora")

    def __str__(self):
        return self.nome_editora
    
    @method_decorator(permission_required('livros.adicionar_editora'))
    def save(self, *args, **kwargs):
        # salvando informacoes no db
        super().save(*args, **kwargs)

class Autor(models.Model):
    class Meta: 
        verbose_name_plural = "Autores"
    
    nome_autor = models.CharField(max_length=250, verbose_name="Autor")

    def __str__(self):
        return self.nome_autor
    
    @method_decorator(permission_required('livros.adicionar_autor'))
    def save(self, *args, **kwargs):
        # salvando informacoes no db
        super().save(*args, **kwargs)


class Livro(models.Model):
    nome_livro = models.CharField(max_length = 100, verbose_name="Nome do Livro")
    data_cadastro = models.DateField(auto_now_add= True, verbose_name="Data de Cadastro")
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    descricao_livro = models.TextField(max_length=200, verbose_name="Descrição do Livro", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    livro_imagem = models.ImageField
    
    def __str__(self):
        return self.nome_livro
    
    def quantidade_emprestado(quantidade):
        pass 
    
    @method_decorator(permission_required('livros.adicionar_livro'))
    def save(self, *args, **kwargs):
        # salvando informacoes no db
        super().save(*args, **kwargs)
    

"""@permission_required('livros.adicionar_emprestimo') """  
class Emprestimo(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    nome_emprestado_usuario = models.CharField(max_length=150, verbose_name="Nome Usuário Cadastrado")
    data_emprestimo = models.DateField(verbose_name="Data de Empréstimo", auto_now_add=True)
    data_devolucao = models.DateField(verbose_name="Data de Devolução")
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
 
    def __str__(self):
        return self.nome_emprestado_usuario
    
    @method_decorator(permission_required('livros.adicionar_emprestimo'))
    def save(self, *args, **kwargs):
        # salvando informacoes no db
        super().save(*args, **kwargs)
  
 
def verificar_livros_emprestados():
        
    total_livros = Livro.objects.count()
    livros_emprestados = Emprestimo.objects.count()

    return livros_emprestados

# Chamada da função para obter o número de livros emprestados
livros_emprestados = verificar_livros_emprestados()

print(f"Total de livros emprestados: {livros_emprestados}")
