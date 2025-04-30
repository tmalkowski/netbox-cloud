from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.forms.fields import CommentField


class AzureResourceBase(NetBoxModel):
    name = models.CharField("Name", max_length=100)
    azure_id = models.CharField("Azure ID", max_length=100, unique=True, blank=True)
    comments = models.TextField("Comments", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

