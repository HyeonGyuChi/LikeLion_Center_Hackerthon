from django import forms
from .models import ResumeInfo, Resume

class ResumeInfoForm(forms.ModelForm):
    class Meta:
        model = ResumeInfo
        fields = ['writer_name', 'writer_address', 'writer_phone', 'writer_email']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('resume_name', 'file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False