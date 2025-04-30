from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField


class CloudOrchestrator(NetBoxModel):
    name =  models.CharField("Name", max_length=100)
    description = models.CharField("Name", max_length=1000)
    comments = CommentField()

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:cloud_orchestrator", kwargs={"pk": self.pk})


class AzureResourceBase(NetBoxModel):
    name = models.CharField("Name", max_length=100)
    azure_id = models.CharField("Azure ID", max_length=100, unique=True, blank=True)
    comments = models.TextField("Comments", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AzureSubscription(AzureResourceBase):
    managed_by = models.CharField("Managed By", max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azuresubscription_view", kwargs={"pk": self.pk})


class AzureResourceGroup(AzureResourceBase):
    location = models.CharField("Location", max_length=100)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azureresourcegroup_view", kwargs={"pk": self.pk})


class AzureVirtualNetwork(AzureResourceBase):
    resource_group = models.ForeignKey(AzureResourceGroup, on_delete=models.CASCADE, related_name="virtual_networks")
    location = models.CharField("Location", max_length=100)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azurevirtualnetwork_view", kwargs={"pk": self.pk})


class AzureSubnet(AzureResourceBase):
    virtual_network = models.ForeignKey(AzureVirtualNetwork, on_delete=models.CASCADE, related_name="subnets")

    prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=False,
        null=False
    )
    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azuresubnet_view", kwargs={"pk": self.pk})

