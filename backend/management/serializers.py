from rest_framework import serializers
from .models import BloodSugarManager, FeedbackManager


class BloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugarManager
        fields = [
            "is_empty_stomach_warning", "is_morning_warning", "is_lunch_warning", "is_evening_warning",
            "empty_stomach", "morning", "lunch", "evening", "feedback",
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackManager
        fields = "__all__"


class BloodSugarAggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugarManager
        fields = [
            "empty_stomach", "morning", "lunch", "evening", "created_at",
        ]
