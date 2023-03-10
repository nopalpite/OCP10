from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name",
                  "last_name", "email", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, data):
        validate_password(password=data, user=User)
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
