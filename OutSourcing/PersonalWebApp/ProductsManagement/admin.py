from django.contrib import admin

from .models import (
    FinishedProduct,
    ActiveWorkingProduct,
    PlannedProduct,
)


class FinishedProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'type', 'date', 'price')


class ActiveWorkingProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'type', 'date', 'price')


class PlannedProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'type', 'date', 'price')


admin.site.register(FinishedProduct, FinishedProductAdmin)
admin.site.register(ActiveWorkingProduct, ActiveWorkingProductAdmin)
admin.site.register(PlannedProduct, PlannedProductAdmin)
