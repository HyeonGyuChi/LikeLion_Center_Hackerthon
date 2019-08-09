from django import forms
from .models import ResumeInfo, Resume

class ResumeInfoForm(forms.ModelForm):
    class Meta:
        model = ResumeInfo
        fields = ['info_name', 'writer_name', 'writer_address', 'writer_phone', 'writer_email']
    def __init__(self, *args, **kwargs):
        super(ResumeInfoForm, self).__init__(*args, **kwargs)
        print(self.fields['info_name'])
        self.fields['info_name'].widget.attrs.update({
            'class': 'infoSection',
            'placeholder': '이력서에 대한 설명',
        })
        
        self.fields['writer_name'].widget.attrs.update({
            'class': 'writerNameSection',
            'placeholder': '작성자 이름',
        })
        self.fields['writer_address'].widget.attrs.update({
            'class': 'writerAddressSection',
            'placeholder': '작성자 주소',
        })
        self.fields['writer_phone'].widget.attrs.update({
            'class': 'writerPhoneNumSection',
            'placeholder': '작성자 전화번호',
        })
        self.fields['writer_email'].widget.attrs.update({
            'class': 'writerEmailSection',
            'placeholder': '작성자 이메일',
        })
        
        self.fields['info_name'].label = ""
        self.fields['writer_name'].label = ""
        self.fields['writer_phone'].label = ""
        self.fields['writer_address'].label = ""
        self.fields['writer_email'].label = ""
        

        
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('resume_name', 'file', 'coin')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False