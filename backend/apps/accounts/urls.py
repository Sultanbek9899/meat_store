from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(("backend.apps.services.urls","backend.apps.services"), namespace="services")),
    path('accounts/', include(("backend.apps.accounts.urls", "backend.apps.accounts"), namespace="accounts")),
]
