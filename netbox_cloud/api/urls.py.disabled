from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()

router.register('azure-subscriptions', views.AzureSubscriptionViewSet)
router.register('azure-resource-groups', views.AzureResourceGroupViewSet)
router.register('azure-virtual-networks', views.AzureVirtualNetworkViewSet)
router.register('azure-subnets', views.AzureSubnetViewSet)

urlpatterns = router.urls
app_name = 'netbox_cloud-api'
