from email.policy import default
from unicodedata import name
import uuid
from django.db import models
import uuid
# Create your models here.
class project(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True,blank=True,default = "default.jpg" )
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=200)
    source_link = models.CharField(max_length=200)
    tags = models.ManyToManyField('tag',blank=True)
    vote_ratio = models.IntegerField(default=0, null = True, blank=True)
    vote_total = models.IntegerField(default=0, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)


class review(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    project = models.ForeignKey(project,on_delete=models.CASCADE)
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.value)

class tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)