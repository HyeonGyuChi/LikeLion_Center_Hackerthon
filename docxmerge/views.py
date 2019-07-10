from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ResumeForm
from .resume_module import resume

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        user_id = User.objects.get(username=request.user.get_username())
        # user_id = request.POST.get('usesrname')
        export_paths = resume(form, user_id)
        return render(request, 'resume_result.html', {'export_paths':export_paths})
    else:
        form = ResumeForm()
    return render(request, 'resume_form.html', {'form':form})
