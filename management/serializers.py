from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class SignupSerializer(serializers.ModelSerializer):
    """
    This serializer defines two fields for signup:
      * username
      * password
      * password2
    It will try to signup the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    
    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token