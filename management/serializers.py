from rest_framework import serializers

from management.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'category']
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, max_length=100)
    # category = serializers.ChoiceField(choices=RESTAURANT_CATEGORY, default='Food')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Restaurant` instance, given the validated data.
    #     """
    #     return Restaurant.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Restaurant` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.save()
    #     return instance