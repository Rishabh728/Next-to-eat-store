# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the default User model
admin.site.unregister(User)

# Create a custom UserAdmin to modify how the User model appears in the admin
class CustomUserAdmin(UserAdmin):
    # Specify which fields to display in the list view
    list_display = ('username', 'email', 'is_active')
    
    # Specify the fields that can be edited directly in the list view
    

    # Optionally, you can add more customization (like adding the 'groups' or 'user_permissions' fields)
    # fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_staff')

    # You can also modify the form used in the admin panel
    # form = CustomUserForm

# Register the User model with the custom UserAdmin
admin.site.register(User, CustomUserAdmin)
