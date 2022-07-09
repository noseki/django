from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = f"{field.label}を入力してください。" 

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',]