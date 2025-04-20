from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'netbox_cloud'

router = DefaultRouter()
router.register(r'azure-subscriptions', views.AzureSubscriptionViewSet)
router.register(r'azure-resource-groups', views.AzureResourceGroupViewSet)
router.register(r'azure-virtual-networks', views.AzureVirtualNetworkViewSet)
router.register(r'azure-subnets', views.AzureSubnetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('azure-subnets/', views.AzureSubnetListView.as_view(), name='azuresubnet_list'),
    path('azure-subnets/<int:pk>/', views.AzureSubnetDetailView.as_view(), name='azuresubnet_detail'),
]

