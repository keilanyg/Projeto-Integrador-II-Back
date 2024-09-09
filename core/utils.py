from django.core.files.base import ContentFile
from django.utils.text import slugify
from rest_framework_simplejwt.tokens import RefreshToken
from typing import TypedDict
import requests
from Biblioteca.settings import env
from django.utils.crypto import get_random_string


class ProfileInfoDTO(TypedDict):
    login: str
    id: int
    avatar_url: int
    name: None | str
    email: None | str


class ClientGithub:
    def get_tokens(self, code: str, state=None):
        url = "https://github.com/login/oauth/access_token"
        headers = {"Accept": "application/json"}

        request_data = {
            "client_id": env.str("GITHUB_CLIENT_ID"),
            "client_secret": env.str("GITHUB_CLIENT_SECRET"),
            "code": code,
        }

        response = requests.post(url, json=request_data, headers=headers)
        return response.json()["access_token"]

    def get_profile_info(self, access_token: str) -> ProfileInfoDTO:
        response = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        )

        return response.json()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def save_avatar_from_github(user, github_avatar_url):
    response = requests.get(github_avatar_url)

    if response.status_code == 200:
        random_string = get_random_string(length=12)
        image_name = slugify(f"{user.first_name}_{random_string}") + ".jpg"

        image_file = ContentFile(response.content)

        user.profile_picture.save(image_name, image_file)
        user.save()
    else:
        print(f"Erro ao baixar a imagem: {response.status_code}")
