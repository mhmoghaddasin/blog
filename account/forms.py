from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from account.validators import validate_username, validate_password


class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(label=_('نام کاربری'), max_length=150, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", }))
    email = forms.EmailField(label=_('ایمیل'), required=True, widget=forms.EmailInput(attrs={"class": "form-control"}),
                             help_text=_('لطفا یک ایمیل معتبر وارد کنید'))
    password = forms.CharField(label=_('کلمه عبور'), widget=forms.PasswordInput(attrs={"class": "form-control"}),
                               required=True)
    password2 = forms.CharField(label=_('تکرار کلمه عبور'), widget=forms.PasswordInput(attrs={"class": "form-control"}),
                                required=True)

    def clean(self):
        password = self.cleaned_data.get('password', None)
        password2 = self.cleaned_data.get('password2', None)
        if password != password2:
            raise ValidationError(_("password don't match"), code='invalid')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username', None)
    #     validate_username(username)
    #     return username

    def clean_password(self):
        password = self.cleaned_data.get('password', None)
        validate_password(password)
        return password
