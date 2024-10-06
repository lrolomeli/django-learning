from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # Pull data from db
    # Transform
    x = 1
    return render(request, 'hello.html', {'name':'Luis R. Lomeli'})
"""
def say_hello(request):
    # Pull data from db
    # Transform
    return HttpResponse("Hello World!")
"""