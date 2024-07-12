from django.db import models


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
    

