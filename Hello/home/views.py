from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        inquiry = request.POST.get('inquiry')
        contact = Contact(name=name, email=email, inquiry=inquiry, date = datetime.today())
        contact.save()
        messages.success(request, "You inquiry has been submitted ! ")
    return render(request,'contact.html')

def icecreams(request):
    return render(request, 'icecreams.html')