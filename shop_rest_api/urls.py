from django.conf.urls import url, include
from rest_framework import routers

from shop_rest_api import views


# Create a router and register our viewsets with it.
router = routers.SimpleRouter()
router.register(r'reviews', views.ReviewListCreate)
router.register(r'items', views.ItemsList)
urlpatterns = router.urls
