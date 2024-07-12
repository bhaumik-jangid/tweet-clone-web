from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.
    
class TweetUserData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_Image = models.ImageField(upload_to='profile_Image/', blank=True, null=True)
    cover_Image = models.ImageField(upload_to='cover_Image/', blank=True, null=True)
    bio = models.TextField(blank=True)
    tweets_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    instagram = models.CharField(max_length=100, blank=True)
    birth_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='tweetImage/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.text[:15]}'