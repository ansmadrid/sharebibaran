from rest_framework import routers, urlpatterns
from .api import ShareViewSet

router = routers.DefaultRouter()
router.register('api/share', ShareViewSet)

urlpatterns = router.urls