from .models import Profile,Image,Comments
from django import forms

class getProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['infor']

class uploadPhoto(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']


class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        exclude =['user', 'picture']