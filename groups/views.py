from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required
from .forms import CategoriesForm
from .models import Categories

# Create your views here.
@login_required
def groups(request, user_id):
    return render(request, 'groups.html', {'user_id': user_id})

@login_required
def individual(request):
    return render(request, 'individual.html')

@login_required
def categories(request, user_id):
    return render(request, 'categories.html', {'user_id': user_id})

@login_required
def addCategory(request, user_id):
    category = get_object_or_404(Categories, pk=user_id)
    if request.method == 'GET':
        return render(request, 'addCategory.html', {'form': CategoriesForm(), 'category': category})
    else:
        try:
            form = CategoriesForm(request.POST)
            newCategory = form.save(commit=False)
            newCategory.user = request.user
            newCategory.category = category
            newCategory.save()
            return redirect('categories', newCategory.categoryName.id)
        except ValueError:
            return render(request, 'addCategory.html', {'form': CategoriesForm(), 'category': category, 'error': 'Bad data in form'})
    
        
