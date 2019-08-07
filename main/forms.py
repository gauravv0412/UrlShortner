from django import forms

class Urlform(forms.Form):
    url = forms.URLField(label = 'Enter URL', required = True, initial='https://')
    # check_box = forms.CheckboxInput()