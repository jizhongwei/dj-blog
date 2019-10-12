from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add= True)
    updated_time = models.DateTimeField(auto_now= True)
    views = models.PositiveIntegerField(default= 0)
    blog_img = models.ImageField(upload_to= 'blog/%Y-%m-%d')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_time',)