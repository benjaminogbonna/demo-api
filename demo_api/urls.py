"""demo_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat-api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chat-api/', include('main.urls')),

    # drf_spectacular
    path('chat-api-auth/', include('rest_framework.urls')),
    path('chat-api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('chat-api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('chat-api/redoc/docs/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc')

]
