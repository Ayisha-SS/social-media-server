from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from posts.models import CreatePost, ViewPost, Categories, User, Customer, Comment


class CreatepostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_by']

class ViewpostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_by']

admin.site.register(CreatePost,CreatepostAdmin)
admin.site.register(ViewPost,ViewpostAdmin)
admin.site.register(Categories)

# admin.site.register(User)



class UserAdmin(DefaultUserAdmin):
    list_display = ['username', 'role', 'email']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )
    list_display = ('username', 'role', 'email','password','is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
admin.site.register(User, UserAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username','role','email','password']

admin.site.register(Comment)
