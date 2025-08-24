from django.http import HttpRequest, HttpResponse

from django.shortcuts import render

def hello(request: HttpRequest):
    return HttpResponse("Hello world ! ")



def test(request: HttpRequest):
    return render(request, "test.html", {
        "title": "测试页面",
    })

def load_home_page(request: HttpRequest):

	return render(request, "/pages/home_page.html", {
        "title": "测试页面",
    })