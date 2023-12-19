from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups, name='groups'),
    path('individual/', views.individual, name='individual'),
    path('categories/', views.categories, name='categories'),
]