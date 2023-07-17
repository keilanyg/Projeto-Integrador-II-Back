from rest_framework import permissions

class IsBibliotecario(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="bibliotecarios"):
            return True
        return False
    
class IsAdministradores(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="administradores"):
            return True
        return False
    
class IsUsuarios(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="usuarios"):
            return True
        return False