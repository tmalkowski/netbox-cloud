from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem


from django.conf import settings

plugin_settings = settings.PLUGINS_CONFIG["netbox_cloud"]

menu_buttons = (
    PluginMenuItem(
        permissions=["netbox_cloud.view_service"],
        link="plugins:netbox_cloud:service_list",
        link_text="Services",
    ),
    PluginMenuItem(
        permissions=["netbox_cloud.view_application"],
        link="plugins:netbox_cloud:application_list",
        link_text="Applications",
    ),
)

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="Service Management",
        groups=(("Services", menu_buttons),),
        icon_class="mdi mdi-cog-outline",
    )
else:
    menu_items = menu_buttons