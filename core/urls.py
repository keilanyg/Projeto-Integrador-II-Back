from django.urls import path, include
from rest_framework import routers
from core.viewsets import user
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns



router = routers.SimpleRouter()

router.register("user", user)



urlpatterns = [
    path("", include(router.urls)),
    
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('accounts/github/', include('allauth.socialaccount.providers.github.urls')),
]
urlpatterns += [path('accounts/github/', include('allauth.socialaccount.providers.github.urls'))]