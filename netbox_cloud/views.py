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

class RelationEditView(generic.ObjectEditView):
    queryset = models.Relation.objects.all()
    form = forms.RelationForm

class PenTestEditView(generic.ObjectEditView):
    queryset = models.PenTest.objects.all()
    form = forms.PenTestForm

class PenTestDeleteView(generic.ObjectDeleteView):
    queryset = models.PenTest.objects.all()

class RelationDeleteView(generic.ObjectDeleteView):
    queryset = models.Relation.objects.all()

class ICDeleteView(generic.ObjectDeleteView):
    queryset = models.IC.objects.all()

class RelationListView(generic.ObjectListView):
    queryset = models.Relation.objects.all()
    table = tables.RelationTable
    filterset = filtersets.RelationFilter
    filterset_form = forms.RelationFilterForm

class RelationView(generic.ObjectView):
    queryset = models.Relation.objects.all()
