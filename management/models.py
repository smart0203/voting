from django.db import models

RESTAURANT_CATEGORY = (
    ("Food", "Food"),
    ("Drink", "Drink"),
    ("Other", "Other")
)


class Restaurant(models.Model):

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=RESTAURANT_CATEGORY, default="Food")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_dt']
