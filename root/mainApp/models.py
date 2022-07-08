import uuid
from django.db import models
import uuid
# Create your models here.
class project(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=200)
    source_link = models.CharField(max_length=200)
    vote_ratio = models.IntegerField(default=0, null = True, blank=True)
    vote_total = models.IntegerField(default=0, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)
