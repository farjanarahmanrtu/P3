from django.shortcuts import HttpResponse
from colorama import init
from termcolor import colored
init()

def hello(request):
    return HttpResponse('Hi, this is practical work 3')
# Create your views here.
