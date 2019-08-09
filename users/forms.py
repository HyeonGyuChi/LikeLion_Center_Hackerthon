from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm as AccountSignup
from allauth.socialaccount.forms import SignupForm as SocialSignup
from django import forms
# from django.contrib.auth.models import User
from .models import User

# account/login.html
class MyCustomLoginForm(LoginForm):
    print('[GET] : Account Login 커스텀 폼 실행되었음')
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'input-login','placeholder':'Email Adreess'})
        self.fields['login'].label = ''
        
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input-login', 'placeholder':'Password'})
        self.fields['password'].label = ''
        
        self.fields['remember'].label = "이메일 저장"
        print(self.fields['remember'])
        
    def login(self, *args, **kwargs):
        # custom override
        
        print('[POST] : Account Login 커스텀 폼 실행되었음')
        return super(MyCustomLoginForm,self).login(*args, **kwargs)


# account/signup.html
class MyCustomSignupForm(AccountSignup):
    print('[GET] : Account Signup 커스텀 폼 실행되었음')
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        print(self.fields)
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'input-signup','placeholder':'Email Adreess'})
        self.fields['email'].label = ''

        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input-signup','placeholder':'username'})
        self.fields['username'].label = ''

        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input-signup','placeholder':'Password1'})
        self.fields['password1'].label = ''

        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input-signup','placeholder':'Password2'})
        self.fields['password2'].label = ''

    def save(self, request):
        print('[POST] : Account Signup 커스텀 폼 실행되었음')
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

# socialaccount/signup.html
class MyCustomSocialSignupForm(SocialSignup):
    def __init__(self, *args, **kwargs):
        super(MyCustomSocialSignupForm, self).__init__(*args, **kwargs)
        # self.fields['email'].widget = forms.TextInput(attrs={'class': 'input-socialsignup','placeholder':'Email Adreess', 'readonly':'readonly'})
        
        print(self.fields)
        print('[GET] : SocialAccount Signup 커스텀 폼 실행되었음')

    def save(self):    
        print('[POST] : SocialAccount Signup 커스텀 폼 실행되었음')
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSocialSignupForm, self).save()
        
        
        # Add your own processing here.

        # You must return the original result.
        return user
