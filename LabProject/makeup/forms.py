from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput())

    def authentication(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        is_authentication = authenticate(username=username, password=password)
        if is_authentication:
            return is_authentication
        return None
