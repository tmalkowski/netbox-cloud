from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from dcim.models import Device
from virtualization.models import VirtualMachine

from . import models
