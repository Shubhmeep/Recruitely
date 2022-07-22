from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to = 'profiles/',default = 'profiles/defaultprofile.png')

    social_github = models.CharField(max_length=200)
    social_linkedin = models.CharField(max_length=200)
    social_twitter = models.CharField(max_length=200)
    social_website= models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user.username)
