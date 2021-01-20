from pymongo import MongoClient
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ###########Global Variables############
#server = 'localhost'
#port = '27017'
#username = ''
#password = ''
database = 'nvd'

def main():

    #connection = MongoClient(server,authSource=database)
    connection = MongoClient("mongodb://USERNAME:PASSWORD@cluster0-shard-00-00.ja3ud.gcp.mongodb.net:27017,cluster0-shard-00-01.ja3ud.gcp.mongodb.net:27017,cluster0-shard-00-02.ja3ud.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-jgyvvk-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = connection[database]
    collection = ''
    UpdateResult = ''
    file_name = input('Please enter collection year: ')
    collection = db['cve_'+file_name]
    cve_data = ''

# Update Cisco IOS Switches
    updateResult = collection.update_many({'product': {'$regex':':ios:'}}, {"$set": {'platform':'switch', 'ios':'ios'}} )
    print("\nUpdating Cisco IOS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco NX-OS Switches
    updateResult = collection.update_many({'product': {'$regex':':nx-os:'}}, {"$set": {'platform':'switch', 'nx_os':'nx-os'}} )
    print("\nUpdating Cisco NX-OS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco IOS-XE Switches
    updateResult = collection.update_many({'product': {'$regex':':ios_xe:'}}, {"$set": {'platform':'switch', 'ios_xe':'ios_xe'}} )
    print("\nUpdating Cisco IOS XE");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco IOS-XR Switches
    updateResult = collection.update_many({'product': {'$regex':':ios_xr:'}}, {"$set": {'platform':'switch', 'ios_xr':'ios_xr'}} )
    print("\nUpdating Cisco IOS XR");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update JUNOS Switches
    updateResult = collection.update_many({'product': {'$regex':':junos:'}}, {"$set": {'platform':'switch', 'junos':'junos'}} )
    print("\nUpdating JunOS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update ARISTA Switches (2)
    updateResult = collection.update_many({'product': {'$regex':':eos:'}}, {"$set": {'platform':'switch', 'arista':'arista'}} )
    print("\nUpdating Arista EOS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

    updateResult = collection.update_many({'product': {'$regex':':extensible_operating_system:'}}, {"$set": {'platform':'switch', 'arista':'arista'}} )
    print("\nUpdating Arista Extensible Operating System");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update ARUBA Switches
    updateResult = collection.update_many({'product': {'$regex':':arubaos:'}}, {"$set": {'platform':'switch', 'aruba':'aruba'}} )
    print("\nUpdating Aruba");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco ISE
    updateResult = collection.update_many({'product': {'$regex':':identity_services_engine_software:'}}, {"$set": {'platform':'switch', 'cisco_ise':'cisco_ise'}} )
    print("\nUpdating Cisco ISE");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Forescout
    updateResult = collection.update_many({'product': {'$regex':':forescout:'}}, {"$set": {'platform':'switch', 'forescout':'forescout'}} )
    print("\nUpdating Forescout");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Update Clearpass
    updateResult = collection.update_many({'product': {'$regex':':clearpass:'}}, {"$set": {'platform':'switch', 'clearpass':'clearpass'}} )
    print("\nUpdating Aruba Clearpass");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Clearpass
    updateResult = collection.update_many({'product': {'$regex':':clearpass_policy_manager:'}}, {"$set": {'platform':'switch', 'clearpass':'clearpass'}} )
    print("\nUpdating Aruba Clearpass");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Fortinac
    updateResult = collection.update_many({'product': {'$regex':':fortinac:'}}, {"$set": {'platform':'switch', 'fortinac':'fortinac'}} )
    print("\nUpdating Fortinac");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco ASA Firewall
    updateResult = collection.update_many({'product': {'$regex':':asa:'}}, {"$set": {'platform':'switch', 'cisco_fw':'cisco_fw'}} )
    print("\nUpdating Cisco ASA Firewall");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco ASA Firewall
    updateResult = collection.update_many({'product': {'$regex':':adaptive_security_appliance:'}}, {"$set": {'platform':'switch', 'cisco_fw':'cisco_fw'}} )
    print("\nUpdating Cisco ASA Firewall");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco Firepower
    updateResult = collection.update_many({'product': {'$regex':':firepower:'}}, {"$set": {'platform':'switch', 'cisco_fw':'cisco_fw'}} )
    print("\nUpdating Cisco Firepower");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco Firepower
    updateResult = collection.update_many({'product': {'$regex':':firepower_threat_defense:'}}, {"$set": {'platform':'switch', 'cisco_fw':'cisco_fw'}} )
    print("\nUpdating Cisco Firepower");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update PaloAlto
    updateResult = collection.update_many({'product': {'$regex':':pan-os:'}}, {"$set": {'platform':'switch', 'palo_alto':'palo_alto'}} )
    print("\nUpdating PaloAlto");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Fortinet
    updateResult = collection.update_many({'product': {'$regex':':fortios:'}}, {"$set": {'platform':'switch', 'fortinet':'fortinet'}} )
    print("\nUpdating Fortinet");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Checkpoint
    updateResult = collection.update_many({'product': {'$regex':':checkpoint:'}}, {"$set": {'platform':'switch', 'checkpoint':'checkpoint'}} )
    print("\nUpdating CheckPoint");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Arista Mojo
    updateResult = collection.update_many({'product': {'$regex':':mojo:'}}, {"$set": {'platform':'switch', 'arista_wifi':'arista_wifi'}} )
    print("\nUpdating Arista Mojo");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':airwave:'}}, {"$set": {'platform':'switch', 'aruba_wifi':'aruba_wifi'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':airwave_network_management:'}}, {"$set": {'platform':'switch', 'aruba_wifi':'aruba_wifi'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':web_management_portal:'}}, {"$set": {'platform':'switch', 'aruba_wifi':'aruba_wifi'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':airwave_glass:'}}, {"$set": {'platform':'switch', 'aruba_wifi':'aruba_wifi'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':aruba_instant:'}}, {"$set": {'platform':'switch', 'aruba_wifi':'aruba_wifi'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco Wifi
    updateResult = collection.update_many({'product': {'$regex':':aironet_access_point_software:'}}, {"$set": {'platform':'switch', 'cisco_wifi':'cisco_wifi'}} )
    print("\nUpdating Cisco Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco Wifi
    updateResult = collection.update_many({'product': {'$regex':':aironet_access_point:'}}, {"$set": {'platform':'switch', 'cisco_wifi':'cisco_wifi'}} )
    print("\nUpdating Cisco Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco Wifi
    updateResult = collection.update_many({'product': {'$regex':':aironet:'}}, {"$set": {'platform':'switch', 'cisco_wifi':'cisco_wifi'}} )
    print("\nUpdating Cisco Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Extreme Wifi
    updateResult = collection.update_many({'product': {'$regex':':extremewireless_wing:'}}, {"$set": {'platform':'switch', 'extreme_wifi':'extreme_wifi'}} )
    print("\nUpdating Extreme Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Extreme Wifi
    updateResult = collection.update_many({'product': {'$regex':':extreme_management_center:'}}, {"$set": {'platform':'switch', 'extreme_wifi':'extreme_wifi'}} )
    print("\nUpdating Extreme Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Extreme Wifi
    updateResult = collection.update_many({'product': {'$regex':':aerohive:'}}, {"$set": {'platform':'switch', 'extreme_wifi':'extreme_wifi'}} )
    print("\nUpdating Aerohive Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

if __name__ == '__main__':
    return_value = main()
