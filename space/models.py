from django.db import models

# Create your models here.
class Space(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    context=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:30]