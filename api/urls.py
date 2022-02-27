from api.views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls