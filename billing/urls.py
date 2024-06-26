from django.urls import path, include
from rest_framework_nested import routers
from .views import CustomerViewSet, ProductViewSet, TransactionViewSet


router = routers.DefaultRouter()

router.register('customers', CustomerViewSet)
router.register('products', ProductViewSet)
router.register('transactions', TransactionViewSet)


urlpatterns = router.urls
