from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'netbox_cloud'

router = DefaultRouter()
router.register(r'azure-subscriptions', views.AzureSubscriptionView)
router.register(r'azure-resource-groups', views.AzureResourceGroupView)
router.register(r'azure-virtual-networks', views.AzureVirtualNetworkView)
router.register(r'azure-subnets', views.AzureSubnetView)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls

