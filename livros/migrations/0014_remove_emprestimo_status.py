# Generated by Django 4.2.1 on 2023-07-25 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0013_alter_livro_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='status',
        ),
    ]
