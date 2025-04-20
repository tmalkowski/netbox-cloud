from netbox.views import generic
from . import models
from . import filtersets
from . import forms
from . import tables

class AzureSubscriptionListView(generic.ObjectListView):
    queryset = models.AzureSubscription.objects.all()
    table = tables.AzureSubscriptionTable

class AzureSubscriptionView(generic.ObjectView):
    queryset = models.AzureSubscription.objects.all()

class AzureResourceGroupListView(generic.ObjectListView):
    queryset = models.AzureResourceGroup.objects.all()
    table = tables.AzureResourceGroupTable

class AzureResourceGroupView(generic.ObjectView):
    queryset = models.AzureResourceGroup.objects.all()

class AzureVirtualNetworkListView(generic.ObjectListView):
    queryset = models.AzureVirtualNetwork.objects.all()
    table = tables.AzureVirtualNetworkTable

class AzureVirtualNetworkView(generic.ObjectView):
    queryset = models.AzureVirtualNetwork.objects.all()

class AzureSubnetListView(generic.ObjectListView):
    queryset = models.AzureSubnet.objects.all()
    table = tables.AzureSubnetTable

class AzureSubnetView(generic.ObjectView):
    queryset = models.AzureSubnet.objects.all()

