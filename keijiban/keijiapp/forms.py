from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = f"{field.label}を入力してください。" 

'''
class SignupForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = ('username','account_image',)
        labels = {'username':"名前",'account_image':"写真アップロード",}

class SignupForm(UserCreationForm):
    avatar = forms.ImageField(upload_to='avatar_icon', blank=True, null=True)
    class Meta:
        model = User
        fields = ['username', 'avatar']
'''