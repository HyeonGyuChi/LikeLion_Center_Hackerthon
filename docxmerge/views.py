from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Resume
from .forms import ResumeForm
from .resume_module import merge

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.save()
        else:
            print(form.errors)
        user_id = User.objects.get(username=request.user.get_username())
        # user_id = request.POST.get('usesrname')
        export_paths = merge(form, user_id)
        return render(request, 'resume_result.html', {'export_paths':export_paths})
    else:
        form = ResumeForm()
    return render(request, 'resume_form.html', {'form':form})

def resume_detail(request, resume_id):
    # resolve_url('blog:post_detail', post.id) # '/blog/105/'
    # resolve_url(post)
    resume = get_object_or_404(Resume, pk=resume_id)
    return render(request, 'resume_detail.html', {'resume': resume})


# def resume_download(request, resume_id):
#     resume = get_object_or_404(Resume, id=resume_id)
#     title = resume.title.encode('euc-kr')
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     # response['Content-Disposition'] = 'attachment; filename=' + title
#     # response.write(resume.contents.encode('euc-kr'))
#     return response