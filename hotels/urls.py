from django.conf.urls import url, include
from rest_framework import routers
from .views import HotelsViewSet

router = routers.DefaultRouter()
router.register(r'hotel', HotelsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
