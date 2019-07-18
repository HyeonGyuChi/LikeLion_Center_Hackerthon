from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.models import User
from .models import ResumeInfo, Resume
from .forms import ResumeForm, UploadFileForm
from .resume_module import merge, handle_uploaded_file

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

# <!-- <a href="{% url 'docxmerge:detail' path.id %}">디테일 페이지</a> -->
def resume_detail(request, resume_id):
    # resolve_url('blog:post_detail', post.id) # '/blog/105/'
    # resolve_url(post)
    resume = get_object_or_404(Resume, pk=resume_id)
    return render(request, 'resume_detail.html', {'resume': resume})

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

# def resume_download(request, resume_id):
#     resume = get_object_or_404(Resume, id=resume_id)
#     title = resume.title.encode('euc-kr')
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     # response['Content-Disposition'] = 'attachment; filename=' + title
#     # response.write(resume.contents.encode('euc-kr'))
#     return response