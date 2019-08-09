import os, json, operator
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from wsgiref.util import FileWrapper
from .models import Resume, ResumeInfo, ResumeMerged
from .forms import ResumeInfoForm, UploadFileForm
from .resume_module import merge
from users.models import User
from users.views import coin_add
from users.views import coin_sub
def resume_make(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # post_text = request.POST.get('form-table')
            form = ResumeInfoForm(request.POST)
            if form.is_valid():
                resume_info = form.save(commit=False)
                resume_info.user = request.user
                resume_info.save()
            else:
                print(form.errors)
            user = User.objects.get(username=request.user.get_full_name())
            resume_merged_list = merge(form, resume_info)
            # return render(request, 'resume_result.html', {'resume_merged_list':resume_merged_list})
            return redirect('docxmerge:result', resume_info.pk)
        else:
            form = ResumeInfoForm()
        return render(request, 'resume_make.html', {'form':form})
    else:
        return redirect('account_login')

def resume_result(request, pk, order_by='download_num', order=0):
    resume_info = ResumeInfo.objects.get(pk=pk)
    if resume_info.user == request.user:
        resume_merged_list = ResumeMerged.objects.filter(resume_info=resume_info)
        key = lambda resume: resume.download_num
        reverse = False
        if order_by == 'like_num':
            key = lambda resume: resume.like_num
        if order == 0:   # 내림차순
            reverse = True
        sorted_resume_merged_list = sorted(resume_merged_list, key=key, reverse=reverse)
        return render(request, 'resume_result.html', {
            'resume_info':resume_info, 
            'resume_merged_list':sorted_resume_merged_list, 
            'order_by':order_by, 
            'order':order})
    else:
        return render(request, 'reject.html')

@login_required
@require_POST # 해당 뷰는 POST method 만 받는다.
def resume_like(request):
    pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    resume = get_object_or_404(Resume, pk=pk)
    resume_like, resume_like_created = resume.like_set.get_or_create(user=request.user)

    if not resume_like_created:
        resume_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': resume.like_count(),
               'message': message,
               'username': request.user.username }

    return HttpResponse(json.dumps(context), content_type="application/json")
    # context를 json 타입으로

@staff_member_required  # 관리자 계정만 템플릿 업로드 가능
def resume_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Resume(resume_name=form.cleaned_data['resume_name'], file=form.cleaned_data['file'], coin=form.cleaned_data['coin'])
            instance.save()
            return redirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, 'resume_upload.html', {'form': form})

def resume_download(request, pk, type):
    resume_merged = get_object_or_404(ResumeMerged, pk=pk)
    cost = resume_merged.resume.coin
    if type == 'pdf':
        content_type = 'application/force-download'
    else:
        content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    wrap = eval('resume_merged.' + type + '_file')
    wrapper = FileWrapper(wrap)
    response = HttpResponse(wrapper, content_type=content_type)
    filename = resume_merged.user.username
    response['Content-Disposition'] = 'inline; filename=' + filename + '.' + type
    resume = get_object_or_404(Resume, pk=resume_merged.resume.pk)
    resume_download, resume_download_created = resume.download_set.get_or_create(user=request.user)
    if resume_download_created:
        download_possible = request.user.coin_sub(cost)     # coin 차감
        if not download_possible:
            resume_download.delete()
            return redirect('users:mypage')
    return response