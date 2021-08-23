from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ParametersFileForm(forms.Form):
    file = forms.FileField()