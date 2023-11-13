from django.urls import path
from . import views

urlpatterns = [
    path('', views.space_home, name = 'space_home'),
]
