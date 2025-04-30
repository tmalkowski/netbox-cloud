from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField
from . import AzureResourceBase


class AzureSubscription(AzureResourceBase):
    managed_by = models.CharField("Managed By", max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azuresubscription_view", kwargs={"pk": self.pk})

