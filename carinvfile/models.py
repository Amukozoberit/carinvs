from sys import modules
from django.db import models

# Create your models here.

carmakes=[('toyota','toyota'),('vits','vits'),('tsunami','tsunami'),('isuzu','isuzu'),('Nissan','Nissan')]

class ShopInventory(models.Model):
    name_of_part=models.CharField(max_length=100,blank=False,default='mcarFix')
    price_of_part= models.DecimalField(max_digits=10, decimal_places=2)
    car_make=models.CharField(choices=carmakes,default='toyota',max_length=50)

    car_model=models.CharField(max_length=100)




class ServicesTable(models.Model):
    service=models.CharField(max_length=100,blank=False,default='Puncture')

    def __str__(self):
        return self.service

class Mechanic(models.Model):
    name_of_mechanic=models.CharField(max_length=100,blank=False)
    # services=models.ForeignKey(ServicesTable,on_delete=models.CASCADE,default=1)
    service=models.ManyToManyField(ServicesTable)

    def __str__(self):
        return self.name_of_mechanic
