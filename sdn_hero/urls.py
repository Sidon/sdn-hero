import os
from django.contrib import admin
from django.urls import include, path
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from sdn_hero import settings
from apps.employee.views import EmployeeViewSet
from apps.company.views import CompanyViewSet

router = DefaultRouter()
router.register('funcionarios', EmployeeViewSet, basename='funcionarios')
router.register('empresas', CompanyViewSet, basename='empresas')

app_name = 'sdn_hero'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('apps.employee.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include((router.urls, 'api-root'),  namespace='api-root')),
]

