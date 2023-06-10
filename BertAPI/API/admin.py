from django.contrib import admin

# AdminPanel libraries
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.cache import cache


#User information 
class AdminPanel(UserAdmin):
    list_display = ('username', 'email', 'token', 'is_staff', 'is_superuser')

    def token(self, obj):
        try:
            token = Token.objects.get(user=obj)
            return token.key
        except Token.DoesNotExist:
            return "-"
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            token = Token.objects.get_or_create(user=obj)

admin.site.unregister(User)
admin.site.register(User, AdminPanel)



