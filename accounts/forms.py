from django import forms
from .models import userProfile


class userProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['file']
