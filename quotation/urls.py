from rest_framework import routers
from quotation import views


router = routers.SimpleRouter()
router.register('currency', views.CurrencyViewSet)
router.register('rate', views.RateViewSet)

rest_urlpatterns = router.urls
