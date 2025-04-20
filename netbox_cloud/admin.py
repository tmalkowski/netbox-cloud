from django.contrib import admin
from .models import AzureSubscription, AzureResourceGroup, AzureVirtualNetwork, AzureSubnet

@admin.register(AzureSubscription)
class AzureSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'azure_id', 'managed_by')

@admin.register(AzureResourceGroup)
class AzureResourceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'azure_id', 'location')

@admin.register(AzureVirtualNetwork)
class AzureVirtualNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'azure_id', 'resource_group', 'location')

@admin.register(AzureSubnet)
class AzureSubnetAdmin(admin.ModelAdmin):
    list_display = ('name', 'azure_id', 'virtual_network', 'prefix')
