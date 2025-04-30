from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField
from . import AzureResourceBase, AzureResourceGroup


class AzureVirtualNetwork(AzureResourceBase):

    resource_group = models.ForeignKey(AzureResourceGroup, on_delete=models.CASCADE, related_name="virtual_networks")

    location = models.CharField("Location", max_length=100)

    prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=False,
        null=False
    )

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azurevirtualnetwork_view", kwargs={"pk": self.pk})

