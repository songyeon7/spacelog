from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Space(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    context = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:30]
