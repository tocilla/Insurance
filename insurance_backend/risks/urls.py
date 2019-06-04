# from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from . import views

app_name = 'risks'

router = DefaultRouter()
router.register('', views.RiskViewSet, base_name='risk')
urlpatterns = router.urls
