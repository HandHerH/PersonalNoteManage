from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View, defaults

from UserManage import models
from UserManage import form_all


# Create your views here.


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
