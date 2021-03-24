from rest_framework import serializers

from ..models import Chef


class ChefsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'