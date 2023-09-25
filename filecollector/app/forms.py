from . import models
from django import forms
class upload(forms.ModelForm):
    class Meta:
        model = models.files
        fields = "__all__"

class Register(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
