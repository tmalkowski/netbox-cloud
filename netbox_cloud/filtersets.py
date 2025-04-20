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

class ICFilter(django_filters.FilterSet):

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        ids = []
        for ic in queryset:
            if value in ic.name:
                ids.append(ic.id)
        return queryset.filter(id__in=ids)

    class Meta:
        model = models.IC

        fields = []


class RelationFilter(NetBoxModelFilterSet):

    class Meta:
        model = models.Relation

        fields = [
            "id",
            "service",
        ]
