from django import forms
from UserManage import models
from django.core.cache import cache

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='再次输入密码', widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码')

    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        verify_code = cleaned_data.get('verify_code')

        if password != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        if not cache.get(f":1:email:{email}"):
            raise forms.ValidationError("验证码过期")
        if str(cache.get(f":1:email:{email}")) != str(verify_code):
            raise forms.ValidationError("验证码错误")
        return cleaned_data
