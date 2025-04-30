from django.urls import path, include
from django.views.generic.base import RedirectView
from netbox.views.generic import ObjectChangeLogView
from rest_framework.routers import DefaultRouter

from . import models, views

app_name = 'netbox_cloud'


urlpatterns = [
    path('',                                     RedirectView.as_view(url="azuresubscription/", permanent=True)),

    path('azure-subscription/',                     views.AzureSubscriptionListView.as_view(),                     name="azuresubscription_list"           ),
    path('azure-subscription/add/',                 views.AzureSubscriptionEditView.as_view(),                     name="azuresubscription_add"            ),
    path('azure-subscription/delete/',              views.AzureSubscriptionBulkDeleteView.as_view(),               name="azuresubscription_bulk_delete"    ),
    path('azure-subscription/<int:pk>/',            views.AzureSubscriptionView.as_view(),                         name="azuresubscription_view"           ),
    path('azure-subscription/<int:pk>/edit/',       views.AzureSubscriptionEditView.as_view(),                     name="azuresubscription_edit"           ), 
    path('azure-subscription/<int:pk>/delete/',     views.AzureSubscriptionDeleteView.as_view(),                   name="azuresubscription_delete"         ),
    path('azure-subscription/<int:pk>/changelog/',  ObjectChangeLogView.as_view(),                                 name='azuresubscription_changelog',     kwargs={'model': models.AzureSubscription }),
    
    path('azure-resourcegroup/',                    views.AzureResourceGroupListView.as_view(),                     name="azureresourcegroup_list"         ),
    path('azure-resourcegroup/add/',                views.AzureResourceGroupEditView.as_view(),                     name="azureresourcegroup_add"          ),
    path('azure-resourcegroup/delete/',             views.AzureResourceGroupBulkDeleteView.as_view(),               name="azureresourcegroup_bulk_delete"  ),
    path('azure-resourcegroup/<int:pk>/',           views.AzureResourceGroupView.as_view(),                         name="azureresourcegroup_view"         ),
    path('azure-resourcegroup/<int:pk>/edit/',      views.AzureResourceGroupEditView.as_view(),                     name="azureresourcegroup_edit"         ),
    path('azure-resourcegroup/<int:pk>/delete/',    views.AzureResourceGroupDeleteView.as_view(),                   name="azureresourcegroup_delete"       ),
    path('azure-resourcegroup/<int:pk>/changelog/', ObjectChangeLogView.as_view(),                                  name='azureresourcegroup_changelog',   kwargs={'model': models.AzureResourceGroup }),
    
    path('azure-virtualnetwork/',                   views.AzureVirtualNetworkListView.as_view(),                    name="azurevirtualnetwork_list"        ),
    path('azure-virtualnetwork/add/',               views.AzureVirtualNetworkEditView.as_view(),                    name="azurevirtualnetwork_add"         ),
    path('azure-virtualnetwork/delete/',            views.AzureVirtualNetworkBulkDeleteView.as_view(),              name="azurevirtualnetwork_bulk_delete" ),
    path('azure-virtualnetwork/<int:pk>/',          views.AzureVirtualNetworkView.as_view(),                        name="azurevirtualnetwork_view"        ),
    path('azure-virtualnetwork/<int:pk>/edit/',     views.AzureVirtualNetworkEditView.as_view(),                    name="azurevirtualnetwork_edit"        ),
    path('azure-virtualnetwork/<int:pk>/delete/',   views.AzureVirtualNetworkDeleteView.as_view(),                  name="azurevirtualnetwork_delete"      ),
    path('azure-virtualnetwork/<int:pk>/changelog/', ObjectChangeLogView.as_view(),                                 name='azurevirtualnetwork_changelog',  kwargs={'model': models.AzureVirtualNetwork }),

    path('azure-subnet/',                           views.AzureSubnetListView.as_view(),                            name="azuresubnet_list"                ),
    path('azure-subnet/add/',                       views.AzureSubnetEditView.as_view(),                            name="azuresubnet_add"                 ),
    path('azure-subnet/delete/',                    views.AzureSubnetBulkDeleteView.as_view(),                      name="azuresubnet_bulk_delete"         ),
    path('azure-subnet/<int:pk>/',                  views.AzureSubnetView.as_view(),                                name="azuresubnet_view"                ),
    path('azure-subnet/<int:pk>/edit/',             views.AzureSubnetEditView.as_view(),                            name="azuresubnet_edit"                ),
    path('azure-subnet/<int:pk>/delete/',           views.AzureSubnetDeleteView.as_view(),                          name="azuresubnet_delete"              ),
    path('azure-subnet/<int:pk>/changelog/',        ObjectChangeLogView.as_view(),                                  name='azuresubnet_changelog',          kwargs={'model': models.AzureSubnet }),

]
