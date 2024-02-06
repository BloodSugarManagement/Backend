from accounts import views
from django.urls import path


urlpatterns = [
    path("google/login-request/", views.GoogleLogin.as_view()),
    path("kakao/login-request/", views.KakaoLogin.as_view()),
    path("naver/login-request/", views.NaverLogin.as_view()),

]
