from django.contrib import admin

from .models import Restaurant, Menu, Employee, Vote


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MenuAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "items")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class VoteAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "employee")


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Vote, VoteAdmin)