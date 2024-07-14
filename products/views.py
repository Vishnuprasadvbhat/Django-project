from django.http import HttpResponse
from django.shortcuts import render
from  .models import  Products

# url Mapping: Calls this functions to /products
# Create your views here.


def index(request):
    products = Products.objects.all()
    # return HttpResponse('Hello World'
    return render(request,'index.html',
                  {'products': products})


def new(request):
    return HttpResponse("New Products")