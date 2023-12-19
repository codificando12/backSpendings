from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def groups(request):
    return render(request, 'groups.html')

@login_required
def individual(request):
    return render(request, 'individual.html')

@login_required
def categories(request):
    return render(request, 'categories.html')
