from django import forms
from django.contrib.auth.models import User
from .models import Video
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        clean = self.cleaned_data
        if clean['password'] != clean['password2']:
            raise forms.ValidationError('Apologies, passwords not a match please re-enter')
        return clean['password2']


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]