from django.contrib import admin
from posts.models import CreatePost,ViewPost,Categories


class CreatepostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_by']

class ViewpostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_by']

admin.site.register(CreatePost,CreatepostAdmin)
admin.site.register(ViewPost,ViewpostAdmin)
admin.site.register(Categories)