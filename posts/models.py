from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"
    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    is_superuser = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            self.is_superuser = False 
        super().save(*args, **kwargs)



class Customer(User):
    base_role = User.Role.USER

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            self.is_superuser = False  
        super(Customer, self).save(*args, **kwargs)

    def welcome(self):
        return "Only for customers"



class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'posts_category'

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField()
    created_by = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content
    

class Like(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts_like'
        unique_together = ('user', 'content_type', 'object_id')  

    def __str__(self):
        return f'{self.user.username} liked {self.content_object}'
    

class CreatePost(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/images/')
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    create_post_comments = models.ManyToManyField('Comment', related_name='create_posts')
    like = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    comments = GenericRelation(Comment)
    likes = GenericRelation(Like)  

    class Meta:
        db_table = 'posts_create'

    def __str__(self):
        return self.title

    def get_like_count(self):
        return self.likes.count()


class ViewPost(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images/')
    description = models.TextField()
    view_post_comments = models.ManyToManyField('Comment', related_name='view_posts')
    like = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    comments = GenericRelation(Comment)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)  

    class Meta:
        db_table = 'posts_view'

    def __str__(self):
        return self.title

    def get_like_count(self):
        return self.likes.count()

   
    



    