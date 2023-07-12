from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from livros.models import Livro, Emprestimo, Categoria, Autor, Editora, Devolucao

adicionar_livro_permission = Permission.objects.create(
    codename='adicionar_livro',
    name='Pode adicionar livro',
    content_type=ContentType.objects.get_for_model(Livro)
)

adicionar_emprestimo_permission = Permission.objects.create(
    codename='adicionar_emprestimo',
    name='Pode adicionar emprestimo',
    content_type=ContentType.objects.get_for_model(Emprestimo)
)

adicionar_categoria_permission = Permission.objects.create(
    codename='adicionar_categoria',
    name='Pode adicionar categoria',
    content_type=ContentType.objects.get_for_model(Categoria)
)

adicionar_autor_permission = Permission.objects.create(
    codename='adicionar_autor',
    name='Pode adicionar autor',
    content_type=ContentType.objects.get_for_model(Autor)
)

adicionar_editora_permission = Permission.objects.create(
    codename='adicionar_editora',
    name='Pode adicionar editora',
    content_type=ContentType.objects.get_for_model(Editora)
)

adicionar_devolucao_permission = Permission.objects.create(
    codename='adicionar_devolucao',
    name='Pode adicionar devolução',
    content_type=ContentType.objects.get_for_model(Devolucao)
)

#chamando os grupos
grupo1 = Group.objects.get(name='administrador')
grupo2 = Group.objects.get(name='bibliotecario')

#criando as permissões 
permissao1 = Permission.objects.get(codename='adicionar_livro')
permissao2 = Permission.objects.get(codename='adicionar_categoria')
permissao3 = Permission.objects.get(codename='adicionar_editora')
permissao4 = Permission.objects.get(codename='adicionar_autor')
permissao5 = Permission.objects.get(codename='adicionar_devolucao')

# Adiciona as permissões ao grupo
grupo2.permissions.add(permissao1, permissao2, permissao3 ,permissao4, permissao5)