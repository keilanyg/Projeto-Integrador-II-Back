from django.contrib.auth.models import Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import User
from core.serializers import BibliotecarioSerializer, UserSerializer
from rest_framework.views import APIView
from .filter import EmprestimoUsuarioFilter
from core.permissions import PostAllowAny
from core.utils import ClientGithub, get_tokens_for_user, save_avatar_from_github
from rest_framework.request import Request
from django.http import HttpResponseRedirect
from pprint import pprint
from Biblioteca.settings import env


# FRONTEND -> Enviar um token

# BACKEND
# /user/me/

# View -> UserViewSet
# Autenticadores -> JWTAuthentication -> Usuario
# request.user = Usuario | request.user.is_authenticated


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = EmprestimoUsuarioFilter
    permission_classes = [IsAuthenticated | PostAllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            first_name=serializer.validated_data.get("first_name"),
            last_name=serializer.validated_data.get("last_name"),
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
        )

        group_name = serializer.validated_data.get("group_name")
        grupo, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(grupo)
        return Response(serializer.data, 201)

    @action(detail=False)
    def me(self, request, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def criar_perfil_bibliotecario(request):
        if request.method == "POST":
            serializer = BibliotecarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)


class UserProviderView(APIView):
    permission_classes = []

    def get(self, request: Request, *args, **kwargs):
        code = request.GET.get("code", None)

        if code is not None:
            github_client = ClientGithub()
            access_token = github_client.get_tokens(code)

            if access_token:
                user_data = github_client.get_profile_info(access_token)
                print(user_data)
                avatar_url = user_data.get("avatar_url")
                id = user_data.get("id")
                
                tokens = None
                user = User.objects.filter(email=id, provider="GITHUB").first()
                if user is not None:
                    tokens = get_tokens_for_user(user)
                else:
                    first_name = user_data.get("name").split(" ")[0]
                    last_name = "".join(user_data.get("name").split(" ")[1:])
                    user = User.objects.create_user_github(
                        email=id,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    grupo, _ = Group.objects.get_or_create(name="usuarios")
                    user.groups.add(grupo)
                    save_avatar_from_github(user, avatar_url)
                    tokens = get_tokens_for_user(user)

                FRONT_END_URL = env.str("FRONT_END_URL")
                access = tokens.get("access")
                refresh = tokens.get("refresh")
                url = (
                    f"{FRONT_END_URL}/usuario/github?access={access}&refresh={refresh}"
                )
                response = HttpResponseRedirect(url)
                return response
        return Response({"detail": "Falha na autenticação."}, status=403)
