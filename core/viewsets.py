from rest_framework.viewsets import ModelViewSet
from core.models import User, AdministradorUser
from core.serializers import UserSerializer, AdministradorUserSerializer
from . filter import EmprestimoUsuarioFilter
from django.shortcuts import render
from datetime import date, timedelta
from livros.models import Emprestimo

class user(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = EmprestimoUsuarioFilter
    
class useradministrador(ModelViewSet):
    queryset = AdministradorUser.objects.all()
    serializer_class = AdministradorUserSerializer
    filter_class = EmprestimoUsuarioFilter

def emprestimos_user(request):
    usuario = request.user  # Obtém o usuário atualmente logado
    emprestimos = Emprestimo.objects.filter(usuario=usuario)

    # Verificar se há empréstimos próximos à data de devolução
    for emprestimo in emprestimos:
        if emprestimo.data_devolucao - date.today() <= timedelta(days=5):
            emprestimo.alerta_devolucao = True
            emprestimo.save()

    return render(request, 'emprestimos.html', {'emprestimos': emprestimos})
