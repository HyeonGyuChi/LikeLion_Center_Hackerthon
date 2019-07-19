import os
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.models import User
from wsgiref.util import FileWrapper
from .models import ResumeInfo, Resume
from .forms import ResumeForm, UploadFileForm
from .resume_module import merge

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
        else:
            print(form.errors)
        user_id = User.objects.get(username=request.user.get_username())
        export_paths = merge(form, user_id)
        return render(request, 'resume_result.html', {'export_paths':export_paths})
        # return HttpResponse(resolve_url('docxmerge:resume_result', export_paths=export_paths))
    else:
        form = ResumeForm()
    return render(request, 'resume_form.html', {'form':form})

def resume_detail(request):
    if request.method == 'POST':
        path = request.POST.get('path')
        return render(request, 'resume_detail.html', {'path': path})
    else:
        path = request.GET.get('path')
        return redirect('/' + path)

def resume_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Resume(resume_name=request.POST['resume_name'], file=request.FILES['file'])
            instance.save()
            return redirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, 'resume_upload.html', {'form': form})

def resume_download(request, type):
    if request.method == 'POST':
        path = request.POST.get('path')
        if type == 'docx':
            path = path[:path.rfind(".")] + '.docx'
            return redirect('../' + path)
        else:
            path = path[path.find("/")+1:]
            path = os.path.abspath(path).replace('\\', '/')
            wrapper = FileWrapper(open(path, 'rb'))
            response = HttpResponse(wrapper, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            return response
