from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Space

# Create your views here.
def home(request):
    spaces = Space.objects.all()
    return render(request, 'space/space_home.html', { 'spaces': spaces })

def detail(request, id):
    space = Space.objects.get(id = id)
    space = get_object_or_404(Space, pk = id)
    return render(request, 'space/space_detail.html', { 'space': space })

def new(request):
    return render(request, 'space/space_new.html')

def create(request):
    new_space = Space()
    new_space.title = request.POST['title']
    new_space.author = request.POST['author']
    new_space.context = request.POST['context']
    new_space.save()
    return redirect('detail', new_space.id)