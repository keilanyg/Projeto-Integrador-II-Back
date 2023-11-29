from django.urls import path, include
from rest_framework import routers
from core.viewsets import user
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
# from .viewsets import SaveGitHubUserData

from rest_framework.routers import DefaultRouter
#from .viewsets import GitHubUserViewSet

router = DefaultRouter()
#router.register(r'api/save-github-user-data', GitHubUserViewSet, basename='github-user')


router = routers.SimpleRouter()

router.register("user", user)



urlpatterns = [
    path("", include(router.urls)),
    
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('accounts/github/', include('allauth.socialaccount.providers.github.urls')),
    #path('api/save-github-user-data/', SaveGitHubUserData.as_view(), name='save_github_user_data'),
]
urlpatterns += [path('accounts/github/', include('allauth.socialaccount.providers.github.urls'))]