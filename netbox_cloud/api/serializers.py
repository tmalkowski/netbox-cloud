from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from netbox.api.fields import ChoiceField, ContentTypeField
from netbox.api.serializers import WritableNestedSerializer
from netbox_cloud import choices

from utilities.api import get_serializer_for_model
from tenancy.api.serializers import TenantSerializer

from dcim.api.serializers import DeviceSerializer
from virtualization.api.serializers import VirtualMachineSerializer

from netbox.api.serializers import NetBoxModelSerializer

from netbox_cloud import models




class RelationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service = serializers.SlugRelatedField(
        slug_field="name", queryset=models.Service.objects.all()
    )

    def get_display(self, obj):
        return obj.name

    class Meta:
        model = models.Relation
        fields = [
            "id",
            "display",
            "name",
            "service",
            "source",
            "source_shape",
            "destination",
            "destination_shape",
            "connector_shape",
            "link_text",
        ]

class PenTestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service = serializers.SlugRelatedField(
        slug_field="name", queryset=models.Service.objects.all()
    )


    class Meta:
        model = models.PenTest
        fields = [
            "id",
            "service",
            "status",
            "comments",
            "date",
            "ticket",
            "report_link"
        ]
class AzureSubscriptionSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureSubscription
        fields = ['id', 'name', 'azure_id', 'managed_by']

class AzureResourceGroupSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureResourceGroup
        fields = ['id', 'name', 'azure_id', 'location']

class AzureVirtualNetworkSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureVirtualNetwork
        fields = ['id', 'name', 'azure_id', 'resource_group', 'location']

class AzureSubnetSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.AzureSubnet
        fields = ['id', 'name', 'azure_id', 'virtual_network', 'prefix']
