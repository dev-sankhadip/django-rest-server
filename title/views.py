from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    params={'name':'sankhadip samanta','home':'bonai'}
    return render(request, 'index.html', params)

def analyze(request):
    text=request.GET.get('text','default')
    punc='`~!@#$%^&*()_+=_[]}{\|;:"<>.,'
    result='';
    for char in text:
        if char not in punc:
            result+=char
    return HttpResponse(result)

def capitalizefirst(request):
    return HttpResponse('cap first')