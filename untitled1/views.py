from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = "<html><body>Hi Djangoooo</body></html>"
    return HttpResponse(html)

def welcome(request):
    html = "<html><body>Welcome to Django</body></html>"
    return HttpResponse(html)

def template_test(request):
    #기본 템플릿폴더
    # 1.admin app
    # 2. 각 앱에  폴더에 있는 template 폴더
    # 3. 설정한 폴더
    return render(request, 'test.html')

# 함수형 뷰 만들기, 템플릿 만들기, URL 연결하기, 브라우저로 접속해보기