from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class UserType(models.Model):
    name = models.CharField(max_length=100)


    
class Bibliotecario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nome} - {self.endereco}'
    
class GitHubUserViewSet(models.Model):
    def post(self, request, *args, **kwargs):
        try:
            github_username = request.data.get('github_username')
            # Outras informações que você deseja salvar

            # Verifique se o usuário já existe no banco de dados com base no github_username
            user_profile, created = User.objects.get_or_create(github_username=github_username)
            # Salve outras informações relevantes no UserProfile

            return Response({'message': 'Informações do usuário salvas com sucesso.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Ocorreu um erro ao salvar as informações do usuário.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        

