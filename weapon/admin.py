from django.contrib import admin
from .models import Weapon
# Register your models here.
admin.site.site_header='INVENTORY ADMIN PANEL'

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display=[
        'name','number'
    ]
