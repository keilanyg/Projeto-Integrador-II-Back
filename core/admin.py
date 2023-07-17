from django.contrib import admin
from .models import User, UserType, AdministradorUser

admin.site.register(UserType)
admin.site.register(User)
admin.site.register(AdministradorUser)
