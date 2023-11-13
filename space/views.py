from django.shortcuts import render
from .models import Space

# Create your views here.
def home(request):
    spaces = Space.objects.all()
    return render(request, 'space/space_home.html', { 'spaces': spaces })