from rest_framework import serializers
from .models import BloodSugarManager, FeedbackManager


class BloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugarManager
        fields = [
            "is_empty_stomach_warning", "is_before_morning_warning", "is_after_morning_warning",
            "is_before_lunch_warning", "is_after_lunch_warning", "is_before_evening_warning",
            "is_after_evening_warning", "empty_stomach", "before_morning", "after_morning",
            "before_lunch", "after_lunch", "before_evening", "after_evening",
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackManager
        fields = "__all__"


class BloodSugarAggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugarManager
        fields = [
            "empty_stomach", "before_morning", "after_morning",
            "before_lunch", "after_lunch", "before_evening", "after_evening",
            "created_at",
        ]
