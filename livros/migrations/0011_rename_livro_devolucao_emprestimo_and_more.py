# Generated by Django 4.2.1 on 2023-07-12 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0010_emprestimo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devolucao',
            old_name='livro',
            new_name='emprestimo',
        ),
        migrations.RemoveField(
            model_name='devolucao',
            name='usuario_devolucao',
        ),
    ]