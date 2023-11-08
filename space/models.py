from django.db import models

# Create your models here.
class space(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    image=models.CharField(max_length=400)
    contents=models.TextField()
    
    