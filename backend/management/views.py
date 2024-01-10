from config.utils import year_standard_format
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.exceptions import ValidationError
from .serializers import BloodSugarSerializer, FeedbackSerializer, BloodSugarAggregateSerializer
from .models import BloodSugarManager, FeedbackManager


class BaseManagementView(RetrieveUpdateDestroyAPIView):
    model = BloodSugarManager
    queryset = BloodSugarManager.objects.all()
    serializer_class = BloodSugarSerializer

    def put(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data["manager"] = request.user.id
        request_data["created_at"] = request_data.get("created_at")

        if not request_data["created_at"]:
            return Response({"message": "날짜를 입력 하세요."}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request_data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self):
        queryset = self.get_queryset()
        request_user = self.request.user
        date_detail = self.get_created_at_date()

        feedback_instance, _ = FeedbackManager.objects.get_or_create(
            manager_id=request_user.id, created_at=date_detail
        )
        obj, _ = queryset.get_or_create(
            manager_id=request_user.id, created_at=date_detail, feedback=feedback_instance
        )
        return obj

    def get_created_at_date(self):
        date_fields = ["year", "month", "day"]

        year = self.kwargs.get("year")  # note: 최적화 필요
        if year:
            self.kwargs["year"] = int(year_standard_format(year))

        date_format = [self.kwargs.get(i) for i in date_fields]

        if any(d is None for d in date_format):
            date_detail = timezone.now().date()
        else:
            date_detail = datetime(*date_format).date()

        return date_detail


class BloodSugarManagementView(BaseManagementView):
    """마이 페이지 접근"""

    model = BloodSugarManager
    queryset = BloodSugarManager.objects.all()
    serializer_class = BloodSugarSerializer


class FeedbackManagementView(BaseManagementView):
    model = FeedbackManager
    queryset = FeedbackManager.objects.all()
    serializer_class = FeedbackSerializer

    def get_object(self):
        queryset = self.get_queryset()
        request_user = self.request.user
        date_detail = self.get_created_at_date()

        feedback_instance, _ = queryset.get_or_create(
            manager_id=request_user.id, created_at=date_detail
        )
        return feedback_instance


class BloodSugarAggregateWithDate(ListAPIView):
    model = BloodSugarManager
    queryset = BloodSugarManager.objects.all()
    serializer_class = BloodSugarAggregateSerializer

    def week_queryset(self):
        user = self.request.user
        one_week_ago = timezone.now() - timezone.timedelta(weeks=1)
        return BloodSugarManager.objects.filter(manager=user, created_at__gte=one_week_ago)

    def month_queryset(self):
        user = self.request.user
        one_month_ago = timezone.now() - relativedelta(months=1)
        return BloodSugarManager.objects.filter(manager=user, created_at__gte=one_month_ago)

    def get_queryset(self):
        date_filter = self.kwargs.get("date_filter")

        filter_options = {
            "week": self.week_queryset,
            "month": self.month_queryset,
        }

        if filter_method := filter_options.get(date_filter):
            return filter_method()
        raise ValidationError({"error": "per week, per month only"})
