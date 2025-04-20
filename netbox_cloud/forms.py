from django import forms

from dcim.models import Device
from circuits.models import Circuit, Provider
from tenancy.models import Tenant
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



