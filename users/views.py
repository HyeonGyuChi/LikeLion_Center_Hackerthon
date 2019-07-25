from django.shortcuts import render, redirect
from django.contrib import auth
from authtools.forms import UserCreationForm
from .models import User
from docxmerge.models import ResumeInfo

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
    resume_infos = ResumeInfo.objects.filter(user=request.user)
    # print(resume_infos)
    return redirect('users:mypage')