import os
import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-target', '-t', required=True, help='Enter the base URL - https://example.service-now.com.')
parser.add_argument('-user', '-u', required=True, help='Enter the username.')
parser.add_argument('-password', '-p', required=True, help='Enter the password.')
args = parser.parse_args()

url = args.target
user = args.user
pwd = args.password

snurl = url + '/api/now/table/'
headers = {"Accept":"application/json"}
 
importtables = open('tables.txt','r')
tables = importtables.read().splitlines() 

for t in tables:
    fullurl = snurl + t
    response = requests.get(fullurl, auth=(user, pwd), headers=headers, timeout=300)
    if response.status_code != 200:
        print("Unable to access. HTTP status code: ", response.status_code)
    print('Attempting to dump: ' + t)
    
    with open(t+'.json','w') as output:
        data = json.loads(response.text)
        json.dump(data, output, indent=4)
    

importtables.close()
