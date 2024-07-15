from django.db import models
from django.contrib.auth.models import AbstractUser


class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'posts_category'

    def __str__(self):
        return self.name
    

class CreatePost(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'posts_create'

    def __str__(self):
        return self.title


class ViewPost(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images/')
    description = models.TextField()
    like = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'posts_view'

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    comments = models.TextField()

    class Meta:
        db_table = 'posts_comment'

    def __str__(self):
        return self.comments
    
    

    

# class CustomUser(AbstractUser):
#     # Add your custom fields here if any
#     # is_admin = models.BooleanField(default=False)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_set',
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_set',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#         swappable = 'AUTH_USER_MODEL'

#     # def __str__(self):
#     #     return self.is_admin

