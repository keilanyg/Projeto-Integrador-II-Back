from django.contrib import admin
from .models import User, UserType

admin.site.register(UserType)
admin.site.register(User)
