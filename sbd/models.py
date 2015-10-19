from django.db import models


class Tvr(models.Model):
    product_id = models.IntegerField(default=0)
    product_supplier_id = models.IntegerField(default=0)
    product_name_rus = models.CharField(max_length=255)
    product_name_eng = models.CharField(max_length=255)
    product_code = models.CharField(max_length=50)
    product_code_analog = models.CharField(max_length=255)
    product_code_replacement = models.CharField(max_length=255)
    product_manufacturer = models.CharField(max_length=50)
    product_car_model = models.CharField(max_length=50)
    product_price_1 = models.CharField(max_length=20)
    product_price_2 = models.CharField(max_length=20)
    product_price_3 = models.CharField(max_length=20)
    product_delivery_time = models.CharField(max_length=10)
    product_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name_rus
