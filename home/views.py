from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
#Username : Hello
#pasword : 123
def index(request):
    context ={
        "variable":"Shruti"
    }
    return render(request,'index.html',context)
#def home(request):
#    return render(request,'index.html')
def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        contact = Contact(name=name, email=email, phone=phone, comment=comment, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Comment has been sent.')
    return render(request,"contact.html")
