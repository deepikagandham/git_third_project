from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
    return HttpResponse('<h1><marquee>I Love My Nana</marquee></h1>')