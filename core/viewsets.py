from rest_framework.viewsets import ModelViewSet
from core.models import User
from core.serializers import UserSerializer, BibliotecarioSerializer
from . filter import EmprestimoUsuarioFilter
from django.shortcuts import render
from datetime import date, timedelta
from livros.models import Emprestimo
from rest_framework.response import Response
from django.contrib.auth.models import Group

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)

from django.utils.crypto import get_random_string, salted_hmac
from django.utils.translation import gettext_lazy as _


class user(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = EmprestimoUsuarioFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        liv= request.data
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(email=request.data['email'],password=request.data['password'], username=request.data['username'])
        user = User.objects.get(email=liv['email'])
        grupo = Group.objects.get(name="usuarios")
        user.groups.add(grupo)
        return Response("ok") 

    """def emprestimos_user(request):
        usuario = request.user  # Obtém o usuário atualmente logado
        emprestimos = Emprestimo.objects.filter(usuario=usuario)

        # Verificar se há empréstimos próximos à data de devolução
        for emprestimo in emprestimos:
            if emprestimo.data_devolucao - date.today() <= timedelta(days=5):
                emprestimo.alerta_devolucao = True
                emprestimo.save()"""

    def criar_perfil_bibliotecario(request):
        if request.method == 'POST':
            serializer = BibliotecarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)