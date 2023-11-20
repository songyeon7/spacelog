# forms.py

from django import forms
from .models import Space, Category

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['title', 'author', 'context', 'image', 'category']  # 필요한 모든 필드를 포함


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']