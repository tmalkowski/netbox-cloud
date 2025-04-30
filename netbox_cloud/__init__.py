from netbox.plugins import PluginConfig
from .version import __version__


class NetboxCloudPluginConfig(PluginConfig):
    name = 'netbox_cloud'
    base_url = 'netbox_cloud'
    verbose_name = 'Cloud Providers'
    description = 'Cloud inventory integration'
    version = __version__
    author = 'Tony Malkowski'
    author_email = 'tony@txstate.edu'
    required_settings = []
    default_settings = {
        "top_level_menu": True
    }

    def ready(self):
        super().ready()


config = NetboxCloudPluginConfig # noqa
