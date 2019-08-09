from django import forms
from .models import ResumeInfo, Resume

class ResumeInfoForm(forms.ModelForm):
    class Meta:
        model = ResumeInfo
        fields = '__all__'
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
            'placeholder': '전화번호 010-0000-0000',
        })
        self.fields['writer_email'].widget.attrs.update({
            'class': 'writerEmailSection',
            'placeholder': '작성자 이메일',
        })
        self.fields['writer_career_whenstart'].widget.attrs.update({
            'class': 'writerCareerWhenstartSection',
            'placeholder': '20xx.xx.xx',
        })
        self.fields['writer_career_whenstop'].widget.attrs.update({
            'class': 'writerCareerWhenstopSection',
            'placeholder': '20xx.xx.xx',
        })
        self.fields['writer_career_name'].widget.attrs.update({
            'class': 'writerCareerNameSection',
            'placeholder': '경력지 이름',
        })
        self.fields['writer_career_detail'].widget.attrs.update({
            'class': 'writerCareerDetailSection',
            'placeholder': '경력지에서의 경험 및 기타',
        })
        self.fields['writer_career_title'].widget.attrs.update({
            'class': 'writerCarrerTitleSection',
            'placeholder': '경력지에서의 직함',
        })
        self.fields['writer_school_whenstart'].widget.attrs.update({
            'class': 'writerSchoolWhenstartSection',
            'placeholder': '20xx.xx.xx',
        })
        self.fields['writer_school_whenstop'].widget.attrs.update({
            'class': 'writerSchoolWhenstopSection',
            'placeholder': '20xx.xx.xx',
        })
        self.fields['writer_school_name'].widget.attrs.update({
            'class': 'writerSchoolNameSection',
            'placeholder': '학교 이름(최종)',
        })
        self.fields['writer_school_study'].widget.attrs.update({
            'class': 'writerSchoolStudySection',
            'placeholder': '전공및 학위',
        })
        self.fields['writer_prizeandetc_whenstart'].widget.attrs.update({
            'class': 'writerPrizeandetcWhenstartSection',
            'placeholder': '20xx.xx.xx',
        })
        self.fields['writer_prizeandetc_whenstop'].widget.attrs.update({
            'class': 'writerPrizeandetcWhenstopSection',
            'placeholder': '20xx.xx.xx',
        })
        self.fields['writer_prizeandetc_name'].widget.attrs.update({
            'class': 'writerPrizeandetcNameSection',
            'placeholder': '수상내역',
        })
        self.fields['writer_prizeandetc_detail'].widget.attrs.update({
            'class': 'writerPrizeandetcSection',
            'placeholder': '수상 내용',
        })
        self.fields['writer_ability_name'].widget.attrs.update({
            'class': 'writerAbilityNameSection',
            'placeholder': '자격증',
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