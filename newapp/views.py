from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def addnew(request):
    formset = CustomerForm()



    return render(request, 'addnew.html',{'formset':formset})

def homepage(request):
    """
    Function responds to website root HTTP request

    Returns index.html template - no db data returned
    
    """

    x = Customer.objects.all()

    for val in x:
        print(val)
    return render(request, 'index.html',{'data': x})