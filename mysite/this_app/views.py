from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h2>Hello</h2>')

def home(request):
    return HttpResponse('<h2>Home</h2>')

def posts(request):
    return HttpResponse('<h2>Posts</h2>')

def post(request):
    return HttpResponse('<h2>Post title</h2>')

def profile(request):
    return HttpResponse('<h2>User Profile</h2>')