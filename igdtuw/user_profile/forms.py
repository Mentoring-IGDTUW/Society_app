from django import forms
from .models import Profile_home


class Profile_homeForm(forms.ModelForm):
    class Meta:
        model = Profile_home
        fields = ('name', 'en_no', 'year', 'branch', 'email', 'ph_no', 'password', 'profile_pic')