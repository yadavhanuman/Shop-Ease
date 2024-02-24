from django.db import models
from .catagory import Catagory

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1, null=True, blank=True)
    discription = models.CharField(max_length=300)
    images = models.ImageField(upload_to='uploads/products/')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all

    @staticmethod
    def get_all_products_by_catagoryid(catagory_id):
        if catagory_id:
            return Product.objects.filter(catagory = catagory_id)
        else:
            return Product.get_all_products();
