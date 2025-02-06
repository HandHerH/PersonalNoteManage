from django.shortcuts import render
from django.views import View, defaults


# Create your views here.

class IndexPageView(View):
    def get(self, request):
        return render(request, 'IndexPage/index.html')

    def post(self, request):
        return defaults.page_not_found(request, '访问失败', template_name='404.html')
