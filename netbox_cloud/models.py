from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

class AzureResourceBase(NetBoxModel):
    name = models.CharField("Name", max_length=100)
    azure_id = models.CharField("Azure ID", max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class AzureSubscription(AzureResourceBase):
    managed_by = models.CharField("Managed By", max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azuresubscription", kwargs={"pk": self.pk})

class AzureResourceGroup(AzureResourceBase):
    location = models.CharField("Location", max_length=100)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azureresourcegroup", kwargs={"pk": self.pk})

class AzureVirtualNetwork(AzureResourceBase):
    resource_group = models.ForeignKey(AzureResourceGroup, on_delete=models.CASCADE, related_name="virtual_networks")
    location = models.CharField("Location", max_length=100)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azurevirtualnetwork", kwargs={"pk": self.pk})

class AzureSubnet(AzureResourceBase):
    virtual_network = models.ForeignKey(AzureVirtualNetwork, on_delete=models.CASCADE, related_name="subnets")
    prefix = models.CharField("Prefix", max_length=100)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azuresubnet", kwargs={"pk": self.pk})

