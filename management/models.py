from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant", on_delete = models.CASCADE)
    items = models.TextField()

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_dt']


class Employee(models.Model):
    name = models.CharField(max_length=100)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE, default=0)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_dt']