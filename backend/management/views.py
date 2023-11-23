from config.utils import year_standard_format
from django.utils import timezone
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BloodSugarSerializer
from .models import BloodSugarManager


class BloodSugarManagementView(RetrieveUpdateAPIView):
    """마이 페이지 접근"""

    model = BloodSugarManager
    queryset = BloodSugarManager.objects.all()
    serializer_class = BloodSugarSerializer

    def put(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data["manager"] = request.user.id
        request_data["created_at"] = timezone.now().date()

        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request_data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self):
        queryset = self.get_queryset()
        request_user = self.request.user

        year = self.kwargs.get("year")  # note: 최적화 필요
        month = self.kwargs.get("month")
        day = self.kwargs.get("day")

        year = year_standard_format(year)

        if year is None or month is None or day is None:
            date_detail = timezone.now().date()
        else:
            date_detail = datetime(int(year), int(month), int(day)).date()

        obj, _ = queryset.get_or_create(
            manager_id=request_user.id, created_at=date_detail
        )
        return obj
