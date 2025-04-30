from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField
from . import AzureResourceBase

class AzureResourceGroup(AzureResourceBase):
    location = models.CharField("Location", max_length=100)

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:azureresourcegroup_view", kwargs={"pk": self.pk})

