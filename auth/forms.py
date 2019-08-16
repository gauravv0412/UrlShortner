from django import forms

from auth import models

class Loginform(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'