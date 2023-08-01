from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    name = 'Antonio'
    age = 15
    return render(request, 'index.html', {'name':name, 'age':age})
