from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    description = models.TextField()
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.author} | {self.date}'