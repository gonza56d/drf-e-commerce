from django.urls import path
from rest_framework import routers

from ecommerce.users.views import UserViewSet


router = routers.SimpleRouter()
router.register(r'', UserViewSet)

urlpatters = router.urls
