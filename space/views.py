from django.shortcuts import render, redirect, get_object_or_404
from .forms import SpaceForm, CategoryForm
from .models import Category, Post, Space
from django.core.paginator import Paginator

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # 새 카테고리가 생성된 후 이동할 URL
    else:
        form = CategoryForm()
    return render(request, 'space/category_create.html', {'form': form})

def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'space/category_posts.html', {'category': category, 'posts': posts})


# Create your views here.
def home(request):
    spaces_list = Space.objects.all()
    paginator = Paginator(spaces_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()  # 카테고리 목록 가져오기

    return render(request, 'space/space_home.html', {'page_obj': page_obj, 'categories': categories})


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

