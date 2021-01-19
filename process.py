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
    file_name = input('Please enter filename: ')
    collection = db['cve_'+file_name.replace('.json', '')]
    cve_data = ''
    counter = 0

    with open(file_name, 'r') as jsonfile:
        cve_data = json.loads(jsonfile.read())

    for item in cve_data['CVE_Items']:
        if item['impact'] != {}:
          temp_data = {}
          temp_data['cve'] = str(item['cve']['CVE_data_meta']['ID'])
          temp_data['product'] = str(item['configurations']['nodes'])

          if 'baseMetricV3' in item['impact']:
              temp_data['score'] = item['impact']['baseMetricV3']['cvssV3']['baseScore']
          else:
              temp_data['score'] = item['impact']['baseMetricV2']['cvssV2']['baseScore']

#Add in Platforms
          temp_data['platform'] = 'not_switch'
#Add in Switches
          temp_data['ios'] = 'no'
          temp_data['nx_os'] = 'no'
          temp_data['ios_xe'] = 'no'
          temp_data['ios_xr'] = 'no'
          temp_data['junos'] = 'no'
          temp_data['arista'] = 'no'
          temp_data['aruba'] = 'no'
#Add in NAC
          temp_data['cisco_ise'] = 'no'
          temp_data['forescout'] = 'no'
          temp_data['clearpass'] = 'no'
          temp_data['fortinac'] = 'no'
#Add in Firewalls
          temp_data['cisco_fw'] = 'no'
          temp_data['palo_alto'] = 'no'
          temp_data['fortinet'] = 'no'
          temp_data['checkpoint'] = 'no'
#Add in Wireless
          temp_data['arista_wifi'] = 'no'
          temp_data['aruba_wifi'] = 'no'
          temp_data['cisco_wifi'] = 'no'
          temp_data['extreme_wifi'] = 'no'

          counter = counter + 1
          collection.insert_one(temp_data)

    print("Total Records Entererd: ", counter );

if __name__ == '__main__':
    return_value = main()
