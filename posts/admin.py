from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from posts.models import CreatePost,ViewPost,Categories,LogIn,Signup,Role


class CreatepostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_by']

class ViewpostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_by']

admin.site.register(CreatePost,CreatepostAdmin)
admin.site.register(ViewPost,ViewpostAdmin)
admin.site.register(Categories)
admin.site.register(Signup)
admin.site.register(LogIn)
# admin.site.register(Role)
# admin.site.register(CustomUser)