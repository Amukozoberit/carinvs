from django.contrib import admin

from .models import Mechanic, ServicesTable, ShopInventory

# Register your models here.


admin.site.register(ShopInventory)
admin.site.register(Mechanic)
admin.site.register(ServicesTable)