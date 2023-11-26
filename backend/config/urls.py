"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularYAMLAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
]

user = [
    path('accounts/', include('dj_rest_auth.urls')),
    path("accounts/register/", include("dj_rest_auth.registration.urls")),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
]

docs = [
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("docs/yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc"),
]

app = [
    path("api/", include("management.urls")),
]

urlpatterns.extend(user)
urlpatterns.extend(app)
urlpatterns.extend(docs)
