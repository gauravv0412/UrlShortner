from django import forms

from main import models

class Urlform(forms.ModelForm):
    class Meta :
        model = models.Database
        fields = ['actual_url', 'shortened_url', 'is_private']
        widgets = {
            'actual_url': forms.URLInput(
                attrs={
                    'placeholder': "https://www.google.co.in", 
                    'class': 'form-control',
                }
            ),
            'shortened_url': forms.TextInput(attrs={'placeholder': "localhost:8000/_____", 'class': 'form-control',}),
        }
        error_messages = {
            'shortened_url': {
                'unique': "This CustomUrl is already reserved."
            }
        }
