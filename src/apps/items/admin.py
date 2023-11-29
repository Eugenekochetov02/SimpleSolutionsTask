from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    list_filter = ("price", )


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("date", "first_name", "date")
#     list_filter = ("date", )
