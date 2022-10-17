import django
from django.db import models
import datetime

class Color(models.Model):
    color = models.CharField(max_length=100)

    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"
        db_table = "color"

    def __str__(self):
        return self.color


class Brand(models.Model):
    brand = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        db_table = "brand"
        
    def __str__(self):
        return self.brand


class Type(models.Model):
    type_car = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
        db_table = "type"
        
    def __str__(self):
        return self.type_car
    
    
class Order(models.Model):
    type_car = models.ForeignKey(Type, on_delete=models.CASCADE)
    color_car = models.ForeignKey(Color, on_delete=models.CASCADE)
    date = models.DateField(default=django.utils.timezone.now)
    
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = "order"
        
    def __str__(self):
        return self.pk

