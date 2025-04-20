from netbox.api.viewsets import NetBoxModelViewSet

from netbox_cloud import models
from . import serializers

class AzureSubscriptionViewSet(NetBoxModelViewSet):
    queryset = models.AzureSubscription.objects.all()
    serializer_class = serializers.AzureSubscriptionSerializer

class AzureResourceGroupViewSet(NetBoxModelViewSet):
    queryset = models.AzureResourceGroup.objects.all()
    serializer_class = serializers.AzureResourceGroupSerializer

class AzureVirtualNetworkViewSet(NetBoxModelViewSet):
    queryset = models.AzureVirtualNetwork.objects.all()
    serializer_class = serializers.AzureVirtualNetworkSerializer

class AzureSubnetViewSet(NetBoxModelViewSet):
    queryset = models.AzureSubnet.objects.all()
    serializer_class = serializers.AzureSubnetSerializer
