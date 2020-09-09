from pymongo import MongoClient
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# mongo "mongodb+srv://<server>/<dbname>" --username <username>

# ###########Global Variables############
#server = 'localhost'
#port = '27017'
#username = ''
#password = ''
database = 'nvd'

def main():

    connection = MongoClient(server,authSource=database)
    db = connection[database]
    collection = ''
    file_name = input('Please enter filename: ')
    collection = db['cve_'+file_name.replace('.json', '')]
    cve_data = ''
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

          collection.insert_one(temp_data)

if __name__ == '__main__':
    return_value = main()
