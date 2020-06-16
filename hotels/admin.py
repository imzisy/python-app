# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Hotel
from django.contrib import admin

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    fieldsets = (
        ('Hotel Info', {
            'fields': ('name', 'price', 'duration','expire_date','description',),
        }),
    )

admin.site.register(Hotel, HotelAdmin)
