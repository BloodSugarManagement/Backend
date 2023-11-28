from django.urls import path
from . import views


urlpatterns = [
    path("management/<int:year>/<int:month>/<int:day>/", views.BloodSugarManagementView.as_view(), name="management"),
    path("management/<int:year>/<int:month>/<int:day>/feedback/", views.FeedbackManagementView.as_view(),
         name="feedback"),
    path("management/", views.BloodSugarManagementView.as_view(), name="management"),
    path("management/feedback/", views.FeedbackManagementView.as_view(), name="feedback"),
    path("management/aggregate/<str:date_filter>/", views.BloodSugarAggregateWithDate.as_view(), name="aggregate"),
]
