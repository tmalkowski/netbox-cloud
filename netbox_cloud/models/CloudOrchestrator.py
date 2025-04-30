from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField
from . import AzureResourceBase


class CloudOrchestrator(NetBoxModel):
    name =  models.CharField("Name", max_length=100)
    description = models.CharField("Name", max_length=1000)
    comments = CommentField()

    def get_absolute_url(self):
        return reverse("plugins:netbox_cloud:cloud_orchestrator", kwargs={"pk": self.pk})

