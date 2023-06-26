from django.urls import path, include
from rest_framework import routers
from core.viewsets import user

router = routers.SimpleRouter()

router.register("user", user)

urlpatterns = [
    path("", include(router.urls)),
]
