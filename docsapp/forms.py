from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['writer_name', 'writer_address', 'writer_phone', 'writer_email']
