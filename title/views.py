from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('hello')


# def about(request):
#     return HttpResponse('<h1>hello sankha</h1>  <a href="http://www.google.com">harry bhai</a>')


def index(request):
    return render(request, 'index.html')

def removepunc(request):
    return HttpResponse('removepunc')

def capitalizefirst(request):
    return HttpResponse('cap first')