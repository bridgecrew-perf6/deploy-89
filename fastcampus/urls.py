
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('order/', include('order.urls')),
    path('boss/', include('boss.urls')),
    path('admin/', admin.site.urls),
    path('delivery/', include('delivery.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
