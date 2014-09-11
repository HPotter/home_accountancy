from django.contrib import admin

from models.payments import Payment
from models.stores import StoreType, Store

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass