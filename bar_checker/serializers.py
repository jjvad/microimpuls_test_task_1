from rest_framework import serializers
from .models import PressureRecord
from django.contrib.auth import get_user_model

User = get_user_model()


class PressureRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureRecord
        fields = '__all__'
        read_only_fields = ('user', 'timestamp')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')