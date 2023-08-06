from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer
from .forms import CustomerForm

def test(request):
    html = '<html><body>hello world</body></html>'
    return HttpResponse(html)
def calculation(a,b):
    x = a+b
    return x


def addnew(request):
    if request.method == 'POST':
        formset=CustomerForm(request.POST)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/")
    else:
        formset = CustomerForm()
        x = calculation(10,5)
        return render(request, 'addnew.html',{'formset':formset, 'calc':x})

def homepage(request):
    """
    Function responds to website root HTTP request

    Returns index.html template - no db data returned
    
    """

    x = Customer.objects.all()

    for val in x:
        print(val)
    return render(request, 'index.html',{'data': x})