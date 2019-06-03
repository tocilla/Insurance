# from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
from . import views

app_name = 'risks'

router = DefaultRouter()
router.register('', views.RiskViewSet, base_name='risk')
urlpatterns = router.urls
