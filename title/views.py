from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('hello')


# def about(request):
#     return HttpResponse('<h1>hello sankha</h1>  <a href="http://www.google.com">harry bhai</a>')


def index(request):
    params={'name':'sankhadip samanta','home':'bonai'}
    return render(request, 'index.html', params)

def removepunc(request):
    return HttpResponse('removepunc')

def capitalizefirst(request):
    return HttpResponse('cap first')