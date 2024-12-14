from django.urls import path, include
from rest_framework import routers

from spy_cats import views

router = routers.SimpleRouter()
router.register(r'spy-cats', views.SpyCatsViewSet, basename='spy-cats')

urlpatterns = [
    path('', include(router.urls))
]
