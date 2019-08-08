from allauth.account.forms import LoginForm, SignupForm
from allauth.socialaccount.forms import SignupForm
from django import forms
# from django.contrib.auth.models import User
from .models import User

# account/login.html
class MyCustomLoginForm(LoginForm):
    print('[GET] : Account Login 커스텀 폼 실행되었음')
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'input-login','placeholder':'Email Adreess'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input-login', 'placeholder':'Password'})
        print(self.fields['remember'])
        
    def login(self, *args, **kwargs):
        # custom override
        
        print('[POST] : Account Login 커스텀 폼 실행되었음')
        return super(MyCustomLoginForm,self).login(*args, **kwargs)

'''
class MyCustomSignupForm(forms.Form):
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def signup(self, request, user):
        users = User()
        users.save()
        return user

'''

# account/signup.html
class MyCustomSignupForm(SignupForm):
    print('[GET] : Account Signup 커스텀 폼 실행되었음')


    def save(self, request):
        print('[POST] : Account Signup 커스텀 폼 실행되었음')
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user
'''

# socialaccount/signup.html
class MyCustomSocialSignupForm(SignupForm):

    def save(self):
        print('[GET] : SocialAccount Signup 커스텀 폼 실행되었음')
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSocialSignupForm, self).save()
        print('[POST] : SocialAccount Signup 커스텀 폼 실행되었음')
        # Add your own processing here.

        # You must return the original result.
        return user
'''