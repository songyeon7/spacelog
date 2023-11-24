from django.contrib import admin

# Register your models here.
from .models import Space
from .models import Category

from .models import Post

admin.site.register(Space)

admin.site.register(Category)
admin.site.register(Post)