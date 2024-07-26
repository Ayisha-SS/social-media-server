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
    description = models.TextField(blank=False, null=False)
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
    
class Signup(models.Model):
    username =models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password= models.CharField(max_length=200)

    class Meta:
        db_table = 'posts_signup'

    def __str__(self):
        return self.username

    
class Role(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'


class LogIn(models.Model):
    username = models.EmailField(max_length=200)
    password= models.CharField(max_length=200)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)

    class Meta:
        db_table = 'posts_login'

    def __str__(self):
        return self.username

ROLES = (
    ('USER', 'USER'),
    ('ADMIN', 'ADMIN')
)


class User(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLES, default="USER")

    groups = models.ManyToManyField('auth.Group', related_name='posts_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='posts_user_permissions')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Customer(User):
    base_role = User.role

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super(Customer, self).save(*args, **kwargs)

    def welcome(self):
        return "Only for customers"
    


