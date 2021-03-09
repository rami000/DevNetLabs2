from env import config
import meraki

dashboard = meraki.DashboardAPI(config['MERAKI_KEY'])

def getOrganizationsData():
    request = dashboard.organizations.getOrganizations()
    return request

def printOrganizations():
    request = dashboard.organizations.getOrganizations()
    print(request)
    return request

printOrganizations()



