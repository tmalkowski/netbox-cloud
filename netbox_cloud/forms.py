from django import forms

from dcim.models import Device
from circuits.models import Circuit, Provider
from tenancy.models import Tenant
from ipam.constants import SERVICE_PORT_MIN, SERVICE_PORT_MAX
from virtualization.models import VirtualMachine
from utilities.forms.fields import (
    DynamicModelMultipleChoiceField,
    DynamicModelChoiceField,
    CSVModelMultipleChoiceField,
    NumericArrayField,
    CSVChoiceField,
)
from utilities.forms.widgets import DatePicker

from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelFilterSetForm,
    NetBoxModelBulkEditForm,
    NetBoxModelImportForm,
)

from . import models

class AzureSubscriptionForm(NetBoxModelForm):
    class Meta:
        model = models.AzureSubscription
        fields = ['name', 'azure_id', 'managed_by']

class AzureResourceGroupForm(NetBoxModelForm):
    class Meta:
        model = models.AzureResourceGroup
        fields = ['name', 'azure_id', 'location']

class AzureVirtualNetworkForm(NetBoxModelForm):
    class Meta:
        model = models.AzureVirtualNetwork
        fields = ['name', 'azure_id', 'resource_group', 'location']

class AzureSubnetForm(NetBoxModelForm):
    class Meta:
        model = models.AzureSubnet
        fields = ['name', 'azure_id', 'virtual_network', 'prefix']

class ApplicationForm(NetBoxModelForm):

    ports = NumericArrayField(
        label="Ports",
        base_field=forms.IntegerField(
            min_value=SERVICE_PORT_MIN,
            max_value=SERVICE_PORT_MAX
        ),
    )
    devices = DynamicModelMultipleChoiceField(label="Devices",
        queryset=Device.objects.all(),
        required=False,
    )
    vm = DynamicModelMultipleChoiceField(label="Virtual Machines",
        queryset=VirtualMachine.objects.all(),
        required=False,
    )


    class Meta:
        model = models.Application
        fields = [
            "name",
            "protocol",
            "ports",
            "version",
            "devices",
            "vm",
        ]



class PenTestForm(NetBoxModelForm):

    class Meta:
        model = models.PenTest
        fields = [
            'service',
            'comments',
            'status',
            'date',
            'ticket',
            "report_link",
        ]

        widgets = {
            'date': DatePicker(),
        }

class RelationForm(NetBoxModelForm):

    link_text = forms.CharField(required=False)

    class Meta:
        model = models.Relation
        fields = [
            'service',
            'source_shape',
            'destination_shape',
            "connector_shape",
            "link_text",
        ]

class RelationFilterForm(NetBoxModelFilterSetForm):
    model = models.Relation

    class Meta:
        fields = [
            'service',
            'source',
            'source_shape',
            'destination',
            'destination_shape',
            "connector_shape",
            "link_text",
        ]


