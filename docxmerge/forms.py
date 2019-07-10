from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['date', 'writer_name', 'writer_address', 'writer_phone', 'writer_email']
        date = forms.DateTimeField(input_formats=['%y. %m. %d.'])