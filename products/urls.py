from django.urls import path
from . import views
# adding new urls related to products division in Pyshop

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]