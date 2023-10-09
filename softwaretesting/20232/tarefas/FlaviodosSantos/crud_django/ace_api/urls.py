from django.urls import path, include
from rest_framework import routers
from ace_api import views

router = routers.DefaultRouter()
# router2 = routers.DefaultRouter()

router.register(r'ace_api', views.AceViewSet)
# router2.register(r'list', views.AceListAllViewSet)

urlpatterns = [
    # path('v2/', include(router2.urls), name='home2'),
    path('', include(router.urls), name='home'),
    path('list', views.AceListAllViewSet.as_view(
        {'get': 'list'}), name='list'),
]
