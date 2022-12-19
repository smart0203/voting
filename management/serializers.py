from rest_framework import serializers

from management.models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['name', 'category']


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['restaurant', 'items', 'date']