from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from quotation.urls import rest_urlpatterns as quotation_rest


REST_URL_PATTERNS = (
    quotation_rest
)

ApiSchemaView = get_schema_view(
    openapi.Info(
        title="Quotation System API",
        default_version='V1',
        contact=openapi.Contact(email="angeloasiqueira@gmail.com")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(REST_URL_PATTERNS)),
    path('api/doc/', ApiSchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
