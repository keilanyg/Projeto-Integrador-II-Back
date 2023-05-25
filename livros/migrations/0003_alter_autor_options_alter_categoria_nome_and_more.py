# Generated by Django 4.2.1 on 2023-05-25 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(max_length=250, verbose_name='Editora'),
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('datacadastro', models.DateField(verbose_name='Data de Cadastro')),
                ('datalancamento', models.DateField(verbose_name='Data de Lançamento')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livros.autor', verbose_name='Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livros.categoria', verbose_name='Categoria')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livros.editora', verbose_name='Editora')),
            ],
        ),
    ]
