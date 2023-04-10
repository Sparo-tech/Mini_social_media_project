from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from posts.models import UserPostModel
from Comment.models import Comment



# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=300,blank=True)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    following = models.ManyToManyField(User, blank=True, related_name='following')
    slug = AutoSlugField(populate_from='user')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    # def get_absolute_url(self):
    #     return reverse("profiles:profile-detail-view", kwargs={"slug": self.slug})
    
    count_all_posts = lambda self :  UserPostModel.objects.filter(user=self.user).count()
        
    def count_all_likes(self):
        count_likes=0
        all_post= UserPostModel.objects.filter(user=self.user).all()
        for post in all_post:
            if post.likes.filter(id=self.user.id).exists():
                count_likes+=1
        return count_likes
    
    def comment_count(self):
        all_comment = Comment.objects.filter(author=self.user).all().count()
        return all_comment
    
    def total_posts_likes_count(self):
        all_posts = UserPostModel.objects.filter(user=self.user)
        count=0
        for post in all_posts:
            count+=post.likes.count()
        return count
    
    def get_avatar_url(self):
        try:
            url =self.avatar.url
        except:
            url=''
        return url
    
    count_followers = lambda self : self.followers.all().count()
    
    count_following = lambda self : self.following.all().count() 

    
    
    all_following = lambda self: self.following.all()
    

    all_followers = lambda self : self.follwers.all()
        
    
   

    
