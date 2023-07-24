from rest_framework.viewsets import ModelViewSet
from core.models import User, AdministradorUser
from core.serializers import UserSerializer, AdministradorUserSerializer
from . filter import EmprestimoUsuarioFilter
from django.shortcuts import render
from datetime import date, timedelta
from livros.models import Emprestimo
from rest_framework.response import Response
from django.contrib.auth.models import Group

class user(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = EmprestimoUsuarioFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        liv= request.data
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(email=liv['email'])
        headers = self.get_success_headers(serializer.data)
        grupo = Group.objects.get(name="usuarios")
        user.groups.add(grupo)
        user.save()
        return Response(serializer.data, headers=headers)
    
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
