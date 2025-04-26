# filepath: d:\Python Project\Django\Hello\home\views.py
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context={
        'variable': 'This is a variable passed from the view to the template.'
    }
    # messages.success(request, "This is a success message.")
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world! This is the home page.")
    

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()  # Save the contact entry to the database  
        messages.success(request, "Your Message has Been Sent !!")
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def specialoffers(request):
    return render(request, 'specialoffers.html')

def combo(request):
    return render(request, 'combo.html')

def offer(request):
    return render(request, 'offer.html')