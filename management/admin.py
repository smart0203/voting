from django.contrib import admin

from .models import Restaurant, Menu


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


class MenuAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "items", "date")


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)