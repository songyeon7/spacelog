from django import forms
from .models import Space

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['title', 'author', 'context', 'image']