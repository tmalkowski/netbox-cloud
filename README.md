# Netbox Cloud Resource Inventory Plugin

This plugin extends Netbox to manage cloud resources, starting with Azure. It aims to provide a structured way to organize and manage cloud resources alongside existing Netbox objects.

## Objectives

- Implement custom object types for cloud resources such as Azure Subscriptions, Resource Groups, Virtual Networks, and Subnets.
- Ensure seamless integration with Netbox's existing features like tags, comments, and changelogs.
- Provide a REST API for CRUD operations on cloud resources.
- Facilitate easy addition of new cloud providers and resource types in the future.

## Azure Resource Types

1. **Azure Subscription**
   - Fields: Name, Azure ID, Managed By (e.g., Terraform, Ansible)

2. **Azure Resource Group**
   - Fields: Name, Azure ID, Location

3. **Azure Location**
   - Fields: Name, Description

4. **Azure Virtual Network**
   - Fields: Name, Azure ID, Resource Group, Location

5. **Azure Subnet**
   - Fields: Name, Azure ID, Virtual Network, Prefix

## Development Guidelines

- Follow Netbox's best practices for model and API design.
- Use a base class for common fields like Azure ID and Name.
- Implement a navigation menu for easy access to cloud resources.
- Ensure the UI and API provide consistent data views.

## Future Enhancements

- Support for additional cloud providers like AWS and GCP.
- Integration with external tools for automated resource management.
- Advanced features like VM and container orchestration.

## Installation

Add the following line to /opt/netbox/local_requirements.txt:
```
netbox_cloud
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```python
PLUGINS = ['netbox_cloud']
```

Run the upgrade script:
```
sudo /opt/netbox/upgrade.sh
```

## Configuration

```python
PLUGINS_CONFIG = {
    "netbox_cloud": {
        "top_level_menu": True,  # Adds a top-level menu item for the plugin
    },
}
```

