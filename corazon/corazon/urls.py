from django.conf.urls import url, include
from rest_framework import routers
from operater.viewsets import *

router = routers.DefaultRouter()
router.register(r'api/patients',PatientViewSet)
router.register(r'api/checkups',CheckupViewSet)
router.register(r'api/sounds',SoundViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
