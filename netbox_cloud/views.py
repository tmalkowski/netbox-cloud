from rest_framework import viewsets
from netbox.views import generic
from . import models
from . import filtersets
from . import forms
from . import tables
from . import serializers

class AzureSubscriptionListView(generic.ObjectListView):
    queryset = models.AzureSubscription.objects.all()
    table = tables.AzureSubscriptionTable

class AzureSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = models.AzureSubscription.objects.all()
    serializer_class = serializers.AzureSubscriptionSerializer

class AzureResourceGroupListView(generic.ObjectListView):
    queryset = models.AzureResourceGroup.objects.all()
    table = tables.AzureResourceGroupTable

class AzureResourceGroupViewSet(viewsets.ModelViewSet):
    queryset = models.AzureResourceGroup.objects.all()
    serializer_class = serializers.AzureResourceGroupSerializer

class AzureVirtualNetworkListView(generic.ObjectListView):
    queryset = models.AzureVirtualNetwork.objects.all()
    table = tables.AzureVirtualNetworkTable

class AzureVirtualNetworkViewSet(viewsets.ModelViewSet):
    queryset = models.AzureVirtualNetwork.objects.all()
    serializer_class = serializers.AzureVirtualNetworkSerializer

class AzureSubnetListView(generic.ObjectListView):
    queryset = models.AzureSubnet.objects.all()
    table = tables.AzureSubnetTable

class AzureSubnetViewSet(viewsets.ModelViewSet):
    queryset = models.AzureSubnet.objects.all()
    serializer_class = serializers.AzureSubnetSerializer

