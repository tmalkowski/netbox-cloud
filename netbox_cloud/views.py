from rest_framework import viewsets
from netbox.views import generic
from . import models
from . import filtersets
from . import forms
from . import tables
from .api import serializers


class AzureSubscriptionListView(generic.ObjectListView):
    queryset = models.AzureSubscription.objects.all()
    table = tables.AzureSubscriptionTable

class AzureSubscriptionView(generic.ObjectView):
    queryset = models.AzureSubscription.objects.all()
    template_name = 'netbox_cloud/azuresubscription.html'

class AzureSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = models.AzureSubscription.objects.all()
    serializer_class = serializers.AzureSubscriptionSerializer

class AzureSubscriptionEditView(generic.ObjectEditView):
    queryset = models.AzureSubscription.objects.all()
    form = forms.AzureSubscriptionForm

class AzureSubscriptionDeleteView(generic.ObjectDeleteView):
    queryset = models.AzureSubscription.objects.all()
    default_return_url = 'plugins:netbox_cloud:azuresubscription_list'

class AzureSubscriptionBulkDeleteView(generic.BulkDeleteView):
    queryset = models.AzureSubscription.objects.all()
    table = tables.AzureSubscriptionTable



class AzureResourceGroupListView(generic.ObjectListView):
    queryset = models.AzureResourceGroup.objects.all()
    table = tables.AzureResourceGroupTable

class AzureResourceGroupView(generic.ObjectView):
    queryset = models.AzureResourceGroup.objects.all()
    template_name = 'netbox_cloud/azureresourcegroup.html'

class AzureResourceGroupViewSet(viewsets.ModelViewSet):
    queryset = models.AzureResourceGroup.objects.all()
    serializer_class = serializers.AzureResourceGroupSerializer

class AzureResourceGroupEditView(generic.ObjectEditView):
    queryset = models.AzureResourceGroup.objects.all()
    form = forms.AzureResourceGroupForm

class AzureResourceGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.AzureResourceGroup.objects.all()
    default_return_url = 'plugins:netbox_cloud:azureresourcegroup_list'

class AzureResourceGroupBulkDeleteView(generic.BulkDeleteView):
    queryset = models.AzureResourceGroup.objects.all()
    table = tables.AzureResourceGroupTable




class AzureVirtualNetworkListView(generic.ObjectListView):
    queryset = models.AzureVirtualNetwork.objects.all()
    table = tables.AzureVirtualNetworkTable

class AzureVirtualNetworkView(generic.ObjectView):
    queryset = models.AzureVirtualNetwork.objects.all()
    template_name = 'netbox_cloud/azurevirtualnetwork.html'

class AzureVirtualNetworkViewSet(viewsets.ModelViewSet):
    queryset = models.AzureVirtualNetwork.objects.all()
    serializer_class = serializers.AzureVirtualNetworkSerializer

class AzureVirtualNetworkEditView(generic.ObjectEditView):
    queryset = models.AzureVirtualNetwork.objects.all()
    form = forms.AzureVirtualNetworkForm

class AzureVirtualNetworkDeleteView(generic.ObjectDeleteView):
    queryset = models.AzureVirtualNetwork.objects.all()
    default_return_url = 'plugins:netbox_cloud:azurevirtualnetwork_list'

class AzureVirtualNetworkBulkDeleteView(generic.BulkDeleteView):
    queryset = models.AzureVirtualNetwork.objects.all()
    table = tables.AzureVirtualNetworkTable



class AzureSubnetListView(generic.ObjectListView):
    queryset = models.AzureSubnet.objects.all()
    table = tables.AzureSubnetTable

class AzureSubnetView(generic.ObjectView):
    queryset = models.AzureSubnet.objects.all()
    template_name = 'netbox_cloud/azuresubnet.html'

class AzureSubnetViewSet(viewsets.ModelViewSet):
    queryset = models.AzureSubnet.objects.all()
    serializer_class = serializers.AzureSubnetSerializer

class AzureSubnetEditView(generic.ObjectEditView):
    queryset = models.AzureSubnet.objects.all()
    form = forms.AzureSubnetForm

class AzureSubnetDeleteView(generic.ObjectDeleteView):
    queryset = models.AzureSubnet.objects.all()
    default_return_url = 'plugins:netbox_cloud:azuresubnet_list'

class AzureSubnetBulkDeleteView(generic.BulkDeleteView):
    queryset = models.AzureSubnet.objects.all()
    table = tables.AzureSubnetTable

