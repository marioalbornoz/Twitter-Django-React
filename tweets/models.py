from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)