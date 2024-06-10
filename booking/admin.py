from django.contrib import admin

from booking.models import Inventory, Test

admin.site.register(Test)
admin.site.register(Inventory)