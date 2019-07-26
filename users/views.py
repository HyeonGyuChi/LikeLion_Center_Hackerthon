from django.shortcuts import render, redirect
from django.contrib import auth
from authtools.forms import UserCreationForm
from .models import User
from docxmerge.models import ResumeInfo, ResumeMerged

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.clean_password2()
            name = form.cleaned_data['name']
            user = User.objects.create_user(
                email=email, 
                password=password, 
                name=name, )
            auth.login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def mypage(request):
    coin = request.user.coin
    resume_merged_list = []
    resume_info_list = ResumeInfo.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'coin':coin, 'resume_info_list':resume_info_list})