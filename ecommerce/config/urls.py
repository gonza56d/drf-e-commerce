from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from ecommerce.authentication.urls import urlpatterns as authentication_urlpaterns
from ecommerce.users.urls import urlpatters as users_urlpatterns

v1 = [
    path('api/v1/auth/', include(authentication_urlpaterns)),
    path('api/v1/users/', include(users_urlpatterns)),
    # OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    *v1,
]
