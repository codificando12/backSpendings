from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.groups, name='groups'),
    path('individual/', views.individual, name='individual'),
    path('<int:user_id>/categories/', views.categories, name='categories'),
    path('<int:user_id>/addCategory/', views.addCategory, name='addCategory'),
]