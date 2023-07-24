from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello, Fly!</h1><br/><h2>this is OPINIONATE DJANGO AS YOU GO</h2>')
