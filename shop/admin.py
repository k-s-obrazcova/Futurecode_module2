from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_supply)
class Pos_supplyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_parametr)
class Pos_parametrAdmin(admin.ModelAdmin):
    pass

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

