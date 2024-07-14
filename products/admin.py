from django.contrib import admin
from .models import Products,Offers

#custmozing the admin panel
# the class ModelAdmin provides methods to manage and modify
# the Admin panel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


# Register your models here.
admin.site.register(Products, ProductAdmin)
admin.site.register(Offers, OffersAdmin)
