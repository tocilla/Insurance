from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'risk_types'

router = DefaultRouter()
router.register('', views.RiskTypeViewSet, base_name='risk_type')
urlpatterns = router.urls
