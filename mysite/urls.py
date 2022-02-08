from django.contrib import admin
from django.urls import include, path
import debug_toolbar

urlpatterns = [
    path('', include('wapl.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]