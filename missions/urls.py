from django.urls import path, include
from rest_framework import routers

from missions import views

router = routers.SimpleRouter()
router.register(r'missions', views.MissionsViewSet, basename='missions')
router.register(r'targets', views.TargetsUpdateOnlyViewSet, basename='targets')

urlpatterns = [
    path('', include(router.urls))
]
