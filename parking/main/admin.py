from django.contrib import admin
from .models import Order, Brand, Type, Color

admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Color)