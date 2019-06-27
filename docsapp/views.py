from django.shortcuts import render, redirect
from .forms import ResumeForm

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        return render(request, 'resume_result.html')
    else:
        form = ResumeForm()
    return render(request, 'resume_form.html', {'form':form})
