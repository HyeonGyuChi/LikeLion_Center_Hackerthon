from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import User
def admin_page(request):
    return redirect('admin')

def index(request):
    return render(request, 'index.html')



