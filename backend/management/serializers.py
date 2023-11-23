from rest_framework import serializers
from .models import BloodSugarManager


class BloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugarManager
        fields = [
            "is_empty_stomach_warning", "is_morning_warning", "is_lunch_warning", "is_evening_warning",
            "empty_stomach", "morning", "lunch", "evening",
        ]
