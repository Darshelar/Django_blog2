from rest_framework import serializers
from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "password", "username", "email", "description", "linkedin_url",
                  "contact_number", "status"]

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            password=validated_data.pop('password'),
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            description=validated_data.pop('description'),
            linkedin_url=validated_data.pop('linkedin_url'),
            status=validated_data.pop('status'),

        )
        return user
