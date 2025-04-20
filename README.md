# Netbox Cloud Plugin
[Netbox](https://github.com/netbox-community/netbox) Plugin for defining cloud resources.

## Compatibility


| Plugin Version | NetBox Version | Tested on |
|----------------|----------------|-----------|
| 0.2.1          | >= 4.2.0       | 4.2.0     |

## Installation

Add the following line to /opt/netbox/local_requirements.txt with
```
netbox_cloud
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['netbox_cloud']
```

Runs /opt/netbox/upgrade.sh

```
sudo /opt/netbox/upgrade.sh
```

## Configuration

```python
PLUGINS_CONFIG = {
    "netbox_cloud": {
        "top_level_menu": True # If set to True the plugin will add a top level menu item for the plugin. If set to False the plugin will add a menu item under the Plugins menu item.  Default is set to True.
    },
}
```

