import json

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View, defaults

from UserManage import models
from UserManage import form_all
from login_strategy import lst

# Create your views here.


class EmailView(View):
    def get(self, request):
        return defaults.page_not_found(request, '访问失败', template_name='404.html')

    def post(self, request):
        email = json.loads(request.body).get('email')
        email_sender = lst.get_strategy('email')
        verify_code = email_sender.generate_code()
        if not email_sender.cache_code(email, verify_code):
            return JsonResponse({"验证信息": "发送失败,请稍后重试"})
        email_sender.send_email(email, '欢迎使用PersonalNote', f'您的验证码:{verify_code}')
        return JsonResponse({"验证信息": "发送成功,请输入验证码完成注册"})


class RegisterView(CreateView):
    model = models.User
    template_name = 'UserManage/registerPage.html'
    form_class = form_all.RegisterForm
    success_url = reverse_lazy('AppUserManage:main')

    def form_valid(self, form):
        print(form.cleaned_data)
        # 验证
        return super().form_valid(form)


class MainPageView(View):
    def get(self, request):
        return render(request, 'UserManage/mainPage.html')

    def post(self, request):
        return defaults.page_not_found(request, '访问失败', template_name='404.html')

# class LoginView():
#     pass
