# from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticated

from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('store.urls')),
]
if settings.DEBUG:
    # newCod
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    schema_view = get_schema_view(
        openapi.Info(
            title="Excavator API",
            default_version='v1',
            description="",
            # terms_of_service="https://www.google.com/policies/terms/",
            # contact=openapi.Contact(email="contact@snippets.local"),
            # license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[],
    )

    import debug_toolbar

    urlpatterns += [
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('__debug__', include(debug_toolbar.urls)),
    ]
