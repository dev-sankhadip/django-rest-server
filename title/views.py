from django.http import HttpResponse

def index(request):
    return HttpResponse('hello')


def about(request):
    return HttpResponse('<h1>hello sankha</h1>  <a href="http://www.google.com">harry bhai</a>')