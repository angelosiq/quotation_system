from rest_framework import routers
from quotation import views


router = routers.SimpleRouter()
router.register('currencies', views.CurrencyViewSet)
router.register('rates', views.RateViewSet)

rest_urlpatterns = router.urls
