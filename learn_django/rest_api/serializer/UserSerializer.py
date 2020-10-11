from rest_framework import serializers

from rest_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'content', 'sex', 'created_time')