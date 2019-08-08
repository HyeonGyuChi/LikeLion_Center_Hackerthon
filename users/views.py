from django.shortcuts import render, redirect
from django.contrib import auth
# from authtools.forms import UserCreationForm
from .models import User
from docxmerge.models import ResumeInfo, ResumeMerged

'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth.login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
'''

def mypage(request):
    usercoin = request.user.usercoin
    resume_merged_list = []
    resume_info_list = ResumeInfo.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'usercoin':usercoin, 'resume_info_list':resume_info_list})

def coin_add(request, amount):
    request.user.coin_add(amount)       # 코인 증가
    return redirect('users:mypage')
