from rest_framework import permissions



class Auth_List_Create(permissions.BasePermission):
    
    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated
            
