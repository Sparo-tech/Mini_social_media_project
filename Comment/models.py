from django.db import models
from posts.models import UserPostModel
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    post= models.ForeignKey(UserPostModel,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_post_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=255)

    def __str__(self):
        return self.comment 
    
