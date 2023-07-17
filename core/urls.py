from django.urls import path, include
from rest_framework import routers
from core.viewsets import user, useradministrador

router = routers.SimpleRouter()

router.register("user", user)
router.register("useradministrador", useradministrador)


urlpatterns = [
    path("", include(router.urls)),
]
