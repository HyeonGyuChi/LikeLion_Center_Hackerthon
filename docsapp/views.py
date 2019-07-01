from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .resume_module import resume

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        export_paths = resume(form)
        return render(request, 'resume_result.html', {'export_paths':export_paths})
    else:
        form = ResumeForm()
    return render(request, 'resume_form.html', {'form':form})

# def resume_result(request):
#     with open('/path/to/my/file.pdf', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#         return response
#     pdf.closed