from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    """
    Function responds to website root HTTP request

    Returns index.html template - no db data returned
    
    """
    name = 'Antonio'
    age = 15

    print(name)
    return render(request, 'index.html', {'name':name, 'age':age,})