from netbox.plugins import PluginMenu, PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_cloud:azuresubscription_list',
        link_text='Azure Subscriptions',
        permissions=['netbox_cloud.view_azuresubscription']
    ),
    PluginMenuItem(
        link='plugins:netbox_cloud:azureresourcegroup_list',
        link_text='Azure Resource Groups',
        permissions=['netbox_cloud.view_azureresourcegroup']
    ),
    PluginMenuItem(
        link='plugins:netbox_cloud:azurevirtualnetwork_list',
        link_text='Azure Virtual Networks',
        permissions=['netbox_cloud.view_azurevirtualnetwork']
    ),
    PluginMenuItem(
        link='plugins:netbox_cloud:azuresubnet_list',
        link_text='Azure Subnets',
        permissions=['netbox_cloud.view_azuresubnet']
    ),
)

menu = PluginMenu(
    label='Azure Resources',
    groups=(('Azure Resources', menu_items),),
    icon_class='mdi mdi-cloud-outline',
)
