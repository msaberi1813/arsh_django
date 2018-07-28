from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.forms import ModelForm

from blog.models import MyUser


class NameForm(forms.ModelForm):
    error_css_class = "error"
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "ایمیل"
        self.fields['name'].label = "نام و نام خانوادگی"
        self.fields['phone'].label = "شماره همراه"
        self.fields['password'].label = "رمز عبور"
        self.fields['avatar'].label = "تصویر پروفایل"
        self.fields['email'].required = True
        self.fields['password'].required = True
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'password', 'phone', 'avatar']
        error_messages = {
            'email': {
                'unique': ('این ایمیل قبلا استفاده شده است.'),
                'required': ('وارد کردن ایمیل ضروری است'),
            }
        }
        widgets = {'password': forms.TextInput(
                     attrs={'type': 'password', 'required': True}
            ),
            'avatar':forms.FileInput(attrs={'name':'avatar'}),
        }

class Nform():
    pass
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()