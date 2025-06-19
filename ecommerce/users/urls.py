from rest_framework import routers

from ecommerce.users.views import UsersAPIView


router = routers.SimpleRouter()
router.register(r'users', UsersAPIView)
urlpatters = router.urls
