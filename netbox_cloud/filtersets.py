import django_filters
from django.db.models import Q
from tenancy.models import Tenant
from dcim.models import Device
from virtualization.models import VirtualMachine

from netbox.filtersets import NetBoxModelFilterSet

from . import models

class AzureSubscriptionFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.AzureSubscription
        fields = ['name', 'azure_id', 'managed_by']

class AzureResourceGroupFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.AzureResourceGroup
        fields = ['name', 'azure_id', 'location']

class AzureVirtualNetworkFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.AzureVirtualNetwork
        fields = ['name', 'azure_id', 'resource_group', 'location']

class AzureSubnetFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.AzureSubnet
        fields = ['name', 'azure_id', 'virtual_network', 'prefix']



class RelationFilter(NetBoxModelFilterSet):

    class Meta:
        model = models.Relation

        fields = [
            "id",
            "service",
        ]
