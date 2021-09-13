from django import forms
from .models import DeviceType

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ParametersFileForm(forms.Form):
    file = forms.FileField()

class CorrentDeviceType(forms.Form):
    selectType = forms.ChoiceField(choices=DeviceType.objects.all())