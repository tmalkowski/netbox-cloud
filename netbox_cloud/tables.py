from django.conf import settings
from packaging import version
import django_tables2 as tables


from netbox.tables import NetBoxTable, ToggleColumn , columns


from . import models

class AzureSubscriptionTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    managed_by = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureSubscription
        fields = ('name', 'azure_id', 'managed_by')

class AzureResourceGroupTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    location = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureResourceGroup
        fields = ('name', 'azure_id', 'location')

class AzureVirtualNetworkTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    resource_group = tables.Column()
    location = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureVirtualNetwork
        fields = ('name', 'azure_id', 'resource_group', 'location')

class AzureSubnetTable(NetBoxTable):
    name = tables.LinkColumn()
    azure_id = tables.Column()
    virtual_network = tables.Column()
    prefix = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.AzureSubnet
        fields = ('name', 'azure_id', 'virtual_network', 'prefix')


class ServiceTable(NetBoxTable):

    name = tables.LinkColumn(verbose_name="Service")
    id = ToggleColumn()
    backup_profile = tables.Column(verbose_name="Backup Profile")

    
    class Meta(NetBoxTable.Meta):
        model = models.Service
        fields = (
            "name",
            "backup_profile",
        )

class ICTable(NetBoxTable):
    id = ToggleColumn()
    assigned_object = tables.LinkColumn(verbose_name="CI")
    obj_type = tables.Column(verbose_name="Type")
    actions = columns.ActionsColumn(actions=("delete",))
    
    class Meta(NetBoxTable.Meta):
        model = models.IC        
        fields = (
            "id",
            "assigned_object",
            "obj_type"
        )

class VulnTable(NetBoxTable):
    id = ToggleColumn()

    class Meta(NetBoxTable.Meta):
        model = models.PenTest        
        fields = (
            "id",
            "ticket",
            "date",
            "status",
        )

        
class RelationTable(NetBoxTable):
    id = ToggleColumn()

    service = tables.LinkColumn(verbose_name="Service")
    source = tables.LinkColumn(verbose_name="Source")
    destination = tables.LinkColumn(verbose_name="Destination")
    
    class Meta(NetBoxTable.Meta):
        model = models.Relation
        fields = [
            "service",
            "source",
            "source_shape",
            "destination",
            "destination_shape",
            "connector_shape",
            "link_text",            
        ]
