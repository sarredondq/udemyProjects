from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.




def contact(request):
    return render(request,"core/contact.html")

def home(request):
    return render(request,"core/home.html")


def about(request):
    return render(request,"core/about.html")