from rest_framework.viewsets import ModelViewSet
from core.models import User
from core.serializers import UserSerializer


class user(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer