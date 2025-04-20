from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'netbox_cloud'

router = DefaultRouter()
router.register(r'azure-subscriptions', views.AzureSubscriptionViewSet)
router.register(r'azure-resource-groups', views.AzureResourceGroupViewSet)
router.register(r'azure-virtual-networks', views.AzureVirtualNetworkViewSet)
router.register(r'azure-subnets', views.AzureSubnetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls

