from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class AddRecordForm(forms.Form):
    PRIORITIES = [
        ('very', 'Very'),
        ('mid', 'In next few days'),
        ('low', 'Slightly')
    ]
    text = forms.CharField(label='What TODO?', min_length=5, max_length=140)
    priority = forms.CharField(label='How important?', widget=forms.Select(choices=PRIORITIES))
