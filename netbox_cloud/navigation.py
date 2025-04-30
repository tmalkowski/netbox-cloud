from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label='Cloud Infrastructure',
    groups=(('Azure', (
        PluginMenuItem(
            link='plugins:netbox_cloud:azuresubscription_list',
            link_text='Azure Subscriptions',
            permissions=['netbox_cloud.view_azuresubscription'],
            buttons=(
                PluginMenuButton(
                    link='plugins:netbox_cloud:azuresubscription_add',
                    title='Add',
                    icon_class='mdi mdi-plus-thick',
                    permissions=['netbox_cloud.add_azuresubscription'],
                ),
            ),
        ),
        PluginMenuItem(
            link='plugins:netbox_cloud:azureresourcegroup_list',
            link_text='Azure Resource Groups',
            permissions=['netbox_cloud.view_azureresourcegroup'],
            buttons=(
                PluginMenuButton(
                    link='plugins:netbox_cloud:azureresourcegroup_add',
                    title='Add',
                    icon_class='mdi mdi-plus-thick',
                    permissions=['netbox_cloud.add_azureresourcegroup'],
                ),
            ),
        ),
        PluginMenuItem(
            link='plugins:netbox_cloud:azurevirtualnetwork_list',
            link_text='Azure Virtual Networks',
            permissions=['netbox_cloud.view_azurevirtualnetwork'],
            buttons=(
                PluginMenuButton(
                    link='plugins:netbox_cloud:azurevirtualnetwork_add',
                    title='Add',
                    icon_class='mdi mdi-plus-thick',
                    permissions=['netbox_cloud.add_azurevirtualnetwork'],
                ),
            ),
        ),
        PluginMenuItem(
            link='plugins:netbox_cloud:azuresubnet_list',
            link_text='Azure Subnets',
            permissions=['netbox_cloud.view_azuresubnet'],
            buttons=(
                PluginMenuButton(
                    link='plugins:netbox_cloud:azuresubnet_add',
                    title='Add',
                    icon_class='mdi mdi-plus-thick',
                    permissions=['netbox_cloud.add_azuresubnet'],
                ),
            ),
        ),
    )),),
    icon_class='mdi mdi-cloud-outline',
)
