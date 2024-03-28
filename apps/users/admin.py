from django.contrib import admin

from apps.users.models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'username', 
        'email', 
        'age', 
        # 'ratin]g'
        )
