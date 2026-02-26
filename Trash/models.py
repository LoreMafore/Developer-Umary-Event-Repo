from django.db import models
from django.contrib.auth.models import User

# Trying to set up models for a blog app
# Confused about relationships

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # published = models.BooleanField(default=False)  # should I add this?
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # TODO: add reply functionality - should Comment have a parent field?
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

# TODO: create Category model
# class Category(models.Model):
#     name = 
#     # not sure what fields I need

# TODO: create Tag model for many-to-many relationship
# Getting confused about ManyToManyField vs ForeignKey
