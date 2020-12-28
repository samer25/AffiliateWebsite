from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from forum_app.models import ProfileUser


class RegisterUserForm(UserCreationForm):
    """Register form that can be created user and define class for style """

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for field_name in ['username', 'password1', 'password2', 'email']:
            self.fields[field_name].help_text = None

    class Meta:
        """Using Model User from django auth and specify the fields that we needs """
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class ProfileUserForm(forms.ModelForm):
    """Profile form that  user can create a Profile and define class to fields for style"""

    def __init__(self, *args, **kwargs):
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs = {'class': 'textarea', }

    class Meta:
        model = ProfileUser
        exclude = ['user']


class LoginUserForm(forms.Form):
    """ Login form"""
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
