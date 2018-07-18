from django import forms

class NameForm(forms.Form):
    class Meta:
        pass

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()