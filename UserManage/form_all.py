from django import forms
from UserManage import models


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='再次输入密码', widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return cleaned_data
