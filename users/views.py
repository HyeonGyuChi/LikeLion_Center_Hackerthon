from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User
from docxmerge.models import ResumeInfo, ResumeMerged

def mypage(request):
    print(request.user.email)
    coin = request.user.coin
    resume_merged_list = []
    resume_info_list = ResumeInfo.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'coin':coin, 'resume_info_list':resume_info_list})


