# Generated by Django 4.2.1 on 2023-07-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0011_rename_livro_devolucao_emprestimo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='cover',
            field=models.ImageField(default=1, upload_to='livros/covers/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]