from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Space
from .forms import SpaceForm
from .models import Category
from .forms import CategoryForm

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # 새 카테고리가 생성된 후 이동할 URL
    else:
        form = CategoryForm()
    return render(request, 'space/category_create.html', {'form': form})


# Create your views here.
def home(request):
    spaces = Space.objects.all()
    return render(request, 'space/space_home.html', { 'spaces': spaces })

def detail(request, id):
    space = Space.objects.get(id = id)
    space = get_object_or_404(Space, pk = id)
    return render(request, 'space/space_detail.html', { 'space': space })


def new(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SpaceForm()
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'space/space_new.html', {'form': form, 'categories': categories})


def create(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SpaceForm()
    return render(request, 'space/space_new.html', {'form': form})


def edit(request, id):
    edit_space = Space.objects.get(id=id)
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'space/space_edit.html', {'space': edit_space, 'categories': categories})

def update(request, id):
    if request.method == 'POST':
        update_space = Space.objects.get(id=id)
        update_space.title = request.POST['title']
        update_space.author = request.POST['author']
        update_space.context = request.POST['context']

        # 이미지를 request.FILES에서 받아와서 저장
        if 'image' in request.FILES:
            update_space.image = request.FILES['image']

        update_space.save()
        return redirect('detail', update_space.id)
    else:
        # GET 요청일 경우 적절한 처리
        pass


def delete(request, id):
    delete_space = Space.objects.get(id= id)
    delete_space.delete()
    return redirect('home')

