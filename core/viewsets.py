from rest_framework.viewsets import ModelViewSet
from core.models import User
from core.serializers import UserSerializer
from . filter import EmprestimoUsuarioFilter


class user(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = EmprestimoUsuarioFilter