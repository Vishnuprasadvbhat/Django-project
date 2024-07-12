from django.http import HttpResponse
from django.shortcuts import render

# url Mapping: Calls this functions to /products
# Create your views here.
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse("New Products")