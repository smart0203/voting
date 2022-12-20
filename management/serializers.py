from rest_framework import serializers

from management.models import Restaurant, Menu, Employee, Vote


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name',)


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name',)


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = "__all__"