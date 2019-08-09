from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User
from docxmerge.models import ResumeInfo, ResumeMerged, Resume

def mypage(request):
    usercoin = request.user.usercoin
    resume_merged_list = []
    resume_info_list = ResumeInfo.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'usercoin':usercoin, 'resume_info_list':resume_info_list})

def coin_add(request, amount):
    request.user.coin_add(amount)       # 코인 증가
    return redirect('users:mypage')



def coin_sub(request, amount):
    request.user.coin_sub(amount)          #코인 감소
    return redirect('users:mypage') 