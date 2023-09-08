from django.urls import path, include
from rest_framework import routers
from ace_api.views import AceViewSet

router = routers.DefaultRouter()
router.register(r'ace_api', AceViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]