from django.db import models



class Restaurant(models.Model):
    RESTAURANT_CATEGORY = (
        ("Food", "Food"),
        ("Drink", "Drink"),
        ("Other", "Other")
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=RESTAURANT_CATEGORY, default="Food")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_dt']


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant", on_delete = models.CASCADE)
    items = models.TextField()
    date = models.DateField(auto_now_add=True)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']