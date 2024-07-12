from django.contrib import admin
from .models import Tweet, TweetUserData

# Register your models here.

admin.site.register(Tweet)
admin.site.register(TweetUserData)