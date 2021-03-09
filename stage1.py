from env import config
import meraki
import stage0
import json

organization_name = "DevNet Sandbox"
network_name = "DevNet Sandbox ALWAYS ON"

dashboard = meraki.DashboardAPI(config['MERAKI_KEY'])

def getOrganizationId(organizationName):
    for org in stage0.getOrganizationsData():
        if org['name'] == organization_name:
            organizationId = org['id']

    return organizationId

def getNetwID(network_name, organizationName):
    response = dashboard.organizations.getOrganizationNetworks(getOrganizationId(organization_name), total_pages='all')

    for network in response:
        networkId = ""
        networkNamed = ""
        if network['name'] == networkNamed:
            networkId = network['id']

    return networkId

def devicesInventory(organizationName):
    response = dashboard.organizations.getOrganizationInventoryDevices(getOrganizationId(organization_name), total_pages='all')

    return response

name = ""

if name == "":
    # Generalizes this for given organization name and network name
    network_id = getNetwID(network_name, organization_name)
    inventory = devicesInventory(organization_name)

    # Create a relevant inventory with only devices from the relevant network
    relevant_inventory = []

    for device in inventory:
        if device['networkId'] == network_id:
            relevant_inventory.append(device)

    # Removes irrelevant info from desired inventory
    for relevant_device in relevant_inventory:
        relevant_device.pop('networkId')
        relevant_device.pop('claimedAt')
        relevant_device.pop('orderNumber')

        # Adds source specification
        relevant_device['category'] = 'meraki'

    # Writes the relevant inventory to inventory.json
    with open('inventory.json', 'w') as output_file:
        json.dump(relevant_inventory, output_file)
    
    networkNamed = ""
    organizationName = ""
    print(f"Network Inventory: {networkNamed} - Organization: {organizationName} output in inventory.json")