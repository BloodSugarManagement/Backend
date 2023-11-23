from django.urls import path
from . import views


urlpatterns = [
    path("management/<int:year>/<int:month>/<int:day>/", views.BloodSugarManagementView.as_view(), name="management"),
    path("management/", views.BloodSugarManagementView.as_view(), name="management"),
]
