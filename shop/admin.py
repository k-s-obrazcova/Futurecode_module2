from django.contrib import admin
from .models import Supplier, Supply, Parametr, Tag, Category, Order, Product, Pos_parametr, Pos_order, Pos_supply, Manufacturer, Warehouse, Inventory


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

#
# @admin.register(Supply)
# class SupplyAdmin(admin.ModelAdmin):
#     list_display = ('date_supply', 'supplier')
#
# @admin.register(Parametr)
# class ParametrAdmin(admin.ModelAdmin):
#     list_display = ('name',)
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('buyer_lastname', 'buyer_name', 'buyer_surname', 'comment', 'delivery_address', 'delivery_type', 'date_create', 'date_finish')
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price', 'create_date', 'update_date', 'photo', 'is_exists', 'category')
# @admin.register(Pos_parametr)
# class Pos_parametrAdmin(admin.ModelAdmin):
#     list_display = ('product', 'parametr', 'value')
# @admin.register(Pos_order)
# class Pos_orderAdmin(admin.ModelAdmin):
#     list_display = ('product', 'order', 'count', 'discount')
#
# @admin.register(Pos_supply)
# class Pos_supplyAdmin(admin.ModelAdmin):
#     list_display = ('product', 'supply', 'count')
# @admin.register(Manufacturer)
# class ManufacturerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'country')
#
# @admin.register(Warehouse)
# class WarehouseAdmin(admin.ModelAdmin):
#     list_display = ('location', 'capacity')
#
# @admin.register(Inventory)
# class InventoryAdmin(admin.ModelAdmin):
#     list_display = ('product', 'warehouse', 'quantity')

