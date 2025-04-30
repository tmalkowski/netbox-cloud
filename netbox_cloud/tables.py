from django.conf import settings
from packaging import version
import django_tables2 as tables
from netbox.tables import NetBoxTable, ToggleColumn, columns
from . import models


class AzureSubscriptionTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    comments = tables.Column()
    managed_by = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureSubscription
        fields = ('name', 'azure_id', 'comments', 'managed_by')


class AzureResourceGroupTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    comments = tables.Column()
    location = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureResourceGroup
        fields = ('name', 'azure_id', 'comments', 'location')


class AzureVirtualNetworkTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    comments = tables.Column()
    resource_group = tables.Column()
    prefix = tables.Column()
    location = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureVirtualNetwork
        fields = ('name', 'azure_id', 'comments', 'resource_group', 'location', 'prefix')


class AzureSubnetTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    comments = tables.Column()
    virtual_network = tables.Column()
    prefix = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureSubnet
        fields = ('name', 'azure_id', 'comments', 'virtual_network', 'prefix')

