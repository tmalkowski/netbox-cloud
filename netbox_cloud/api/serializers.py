from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from netbox.api.fields import ChoiceField, ContentTypeField
from netbox.api.serializers import WritableNestedSerializer

from utilities.api import get_serializer_for_model
from tenancy.api.serializers import TenantSerializer

from dcim.api.serializers import DeviceSerializer
from virtualization.api.serializers import VirtualMachineSerializer

from netbox.api.serializers import NetBoxModelSerializer

from netbox_cloud import models




class AzureSubscriptionSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureSubscription
        fields = ['id', 'name', 'azure_id', 'managed_by', 'comments']

class AzureResourceGroupSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureResourceGroup
        fields = ['id', 'name', 'azure_id', 'location', 'comments']

class AzureVirtualNetworkSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureVirtualNetwork
        fields = ['id', 'name', 'azure_id', 'resource_group', 'location', 'comments']

class AzureSubnetSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureSubnet
        fields = ['id', 'name', 'azure_id', 'virtual_network', 'prefix', 'comments']
