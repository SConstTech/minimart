from django.db import models
from django.contrib import admin

# Create your models here.


class InventoryItems(models.Model):
    item_code = models.CharField(max_length=150)
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(decimal_places=4, max_digits=10)
    item_quantity = models.IntegerField()
    stock_arrival_date = models.DateField()
    min_stock = models.IntegerField()
    max_stock = models.IntegerField()
    staff_check = models.BooleanField()

    class Meta:
        verbose_name_plural = "Inventory items"
        verbose_name = "Inventory item"

class InventoryItemsAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'item_price', 'item_quantity', 'stock_arrival_date', 'min_stock', 'max_stock', 'staff_check' )


admin.site.register(InventoryItems,InventoryItemsAdmin)
admin.site.site_header = 'Inventory Management'
