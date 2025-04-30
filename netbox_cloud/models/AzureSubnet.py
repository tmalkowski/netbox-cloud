from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField
from . import AzureResourceBase, AzureVirtualNetwork


class AzureSubnet(AzureResourceBase):
    virtual_network = models.ForeignKey('AzureVirtualNetwork', on_delete=models.CASCADE, related_name="subnets")

    prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=False,
        null=False
    )
    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azuresubnet_view", kwargs={"pk": self.pk})

