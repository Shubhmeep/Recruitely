from django.contrib import admin
from .models import project,review,tag
# Register your models here.
admin.site.register(project)
admin.site.register(review)
admin.site.register(tag)