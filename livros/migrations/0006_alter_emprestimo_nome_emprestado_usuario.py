# Generated by Django 4.2.1 on 2023-07-11 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livros', '0005_remove_emprestimo_nome_emprestado_anonimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário Cadastrado'),
        ),
    ]