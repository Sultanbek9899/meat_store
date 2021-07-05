from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend.apps.services.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name="index"),
]
