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

# ---------------- Switches ------------------------
# Update Cisco IOS Switches
    updateResult = collection.update_many({'product': {'$regex':':cisco:ios:'}}, {"$push": {'vendor':'[cisco]', 'os':'[ios]'}} )
    print("\nUpdating Cisco IOS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco NX-OS Switches
    updateResult = collection.update_many({'product': {'$regex':':cisco:nx-os:'}}, {"$push": {'vendor':'[cisco]', 'os':'[nx-os]'}} )
    print("\nUpdating Cisco NX-OS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco IOS-XE Switches
    updateResult = collection.update_many({'product': {'$regex':':cisco:ios_xe:'}}, {"$push": {'vendor':'[cisco]', 'os':'[ios_xe]'}} )
    print("\nUpdating Cisco IOS XE");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco IOS-XR Switches
    updateResult = collection.update_many({'product': {'$regex':':cisco:ios_xr:'}}, {"$push": {'vendor':'[cisco]', 'os':'[ios_xr]'}} )
    print("\nUpdating Cisco IOS XR");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update JUNOS Switches
    updateResult = collection.update_many({'product': {'$regex':':juniper:junos:'}}, {"$push": {'vendor':'[juniper]', 'os':'[junos]'}} )
    print("\nUpdating JunOS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update ARISTA Switches
    updateResult = collection.update_many({'product': {'$regex':':o:arista:'}}, {"$push": {'vendor':'[arista]', 'os':'[eos]'}} )
    print("\nUpdating Arista EOS");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update ARUBA Switches
    updateResult = collection.update_many({'product': {'$regex':':arubaos:'}}, {"$push": {'vendor':'[aruba]', 'os':'[arubaos]'}} )
    print("\nUpdating Aruba");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Brocade-Extreme Vyette Routers sold to AT&T
    updateResult = collection.update_many({'product': {'$regex':':brocade:vyatta'}}, {"$push": {'vendor':'[extreme]', 'os':'[netiron]'}} )
    print("\nUpdating Extreme");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Brocade-Extreme Netiron Switches
    updateResult = collection.update_many({'product': {'$regex':':brocade:netiron'}}, {"$push": {'vendor':'[extreme]', 'os':'[netiron]'}} )
    print("\nUpdating Extreme");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# ---------------- NAC ------------------------
# Update Cisco ISE
    updateResult = collection.update_many({'product': {'$regex':':cisco:identity_'}}, {"$push": {'vendor':'[cisco]', 'application':'[cisco_ise]'}} )
    print("\nUpdating Cisco ISE");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Forescout
    updateResult = collection.update_many({'product': {'$regex':':forescout:'}}, {"$push": {'vendor':'[forescout]', 'application':'[forescout]'}} )
    print("\nUpdating Forescout");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Clearpass
    updateResult = collection.update_many({'product': {'$regex':'arubanetworks:clearpass'}}, {"$push": {'vendor':'[aruba]', 'application':'[clearpass]'}} )
    print("\nUpdating Aruba Clearpass");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Fortinac
    updateResult = collection.update_many({'product': {'$regex':':fortinac:'}}, {"$push": {'vendor':'[fortinet]', 'application':'[fortinac]'}} )
    print("\nUpdating Fortinac");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# ---------------- Firewall ------------------------
# Update Cisco ASA Firewall (2014 only)
    updateResult = collection.update_many({'product': {'$regex':':cisco:asa'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_fw]'}} )
    print("\nUpdating Cisco ASA Firewall");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco ASA Firewall
    updateResult = collection.update_many({'product': {'$regex':':cisco:adaptive_security'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_fw]'}} )
    print("\nUpdating Cisco ASA Firewall");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Cisco Firepower
    updateResult = collection.update_many({'product': {'$regex':':cisco:firepower'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_fw]'}} )
    print("\nUpdating Cisco Firepower");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update PaloAlto
    updateResult = collection.update_many({'product': {'$regex':':paloaltonetworks:pan-os:'}}, {"$push": {'vendor':'[palo_alto]', 'hardware':'[palo_fw]'}} )
    print("\nUpdating PaloAlto");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Fortinet
    updateResult = collection.update_many({'product': {'$regex':':fortinet:fortios:'}}, {"$push": {'vendor':'[fortinet]', 'os':'[fortios]', 'hardware':'[fortinet_fw]'}} )
    print("\nUpdating Fortinet");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );
# Update Checkpoint
    updateResult = collection.update_many({'product': {'$regex':':checkpoint:'}}, {"$push": {'vendor':'[checkpoint]', 'hardware':'[checkpoint_fw]'}} )
    print("\nUpdating CheckPoint");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# ---------------- WiFi ------------------------
# Update Arista Mojo
    updateResult = collection.update_many({'product': {'$regex':':mojo:'}}, {"$push": {'vendor':'[arista]', 'hardware':'[arista_wifi]'}} )
    print("\nUpdating Arista Mojo");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':arubanetworks:airwave'}}, {"$push": {'vendor':'[aruba]', 'hardware':'[aruba_wifi]'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Update Aruba Wifi
    updateResult = collection.update_many({'product': {'$regex':':arubanetworks:instant'}}, {"$push": {'vendor':'[aruba]', 'hardware':'[aruba_wifi]'}} )
    print("\nUpdating Aruba Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Update Cisco Wifi
    updateResult = collection.update_many({'product': {'$regex':':cisco:aironet'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_wifi]'}} )
    print("\nUpdating Cisco Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Update Extreme Wifi
    updateResult = collection.update_many({'product': {'$regex':':extremenetworks:'}}, {"$push": {'vendor':'[extreme_networks]', 'hardware':'[extreme_wifi]'}} )
    print("\nUpdating Extreme Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Update Extreme Wifi (purchased Aerohive)
    updateResult = collection.update_many({'product': {'$regex':':aerohive:'}}, {"$push": {'vendor':'[extreme_networks]', 'hardware':'[extreme_wifi]'}} )
    print("\nUpdating Aerohive Wifi");
    print("Records Matched:", updateResult.matched_count );
    print("Records Modified:", updateResult.modified_count );

# Meraki products should go here

if __name__ == '__main__':
    return_value = main()
