# Python
import requests
import json
import datetime
from pathlib import Path
import time

# UNIX timestamp in seconds
#now_ms = int( time.time_ns() / 1000000000 ) - 20000

JSON_DIR = Path(__file__).resolve().parent

def get_fids_arrivals():
    # request parameters
    params = {
        'api_key': 'c5076a67-e3d7-474e-8f46-dc3949b2c9e4',
        'arr_icao': 'OEDF',
        'extra':'estimated',
        #'arr_time_ts':now_ms,
    }
    # request endpoint: schedules
    api_base = 'https://airlabs.co/api/v9/flights'
    api_result = requests.get(api_base, params)
    api_response = api_result.json()

    # Logs the date in the log file (THIS WILL NOT PRINT IN THE CLI)    
    print(f'schedule updated at: {datetime.datetime.now()}')

    # save the list in a json file to read it from views.py
    with open(f'{JSON_DIR}/json/fids_arr_dict.json', 'w') as f:
        json.dump(api_response['response'], f)


def get_fids_departures():
    # request parameters
    params = {
        'api_key': 'c5076a67-e3d7-474e-8f46-dc3949b2c9e4',
        'dep_icao': 'OEDF',
    }
    # request endpoint: schedules
    api_base = 'https://airlabs.co/api/v9/schedules'
    api_result = requests.get(api_base, params)
    api_response = api_result.json()

    # Logs the date in the log file (THIS WILL NOT PRINT IN THE CLI)    
    print(f'schedule updated at: {datetime.datetime.now()}')

    # save the list in a json file to read it from views.py
    with open(f'{JSON_DIR}/json/fids_dep_dict.json', 'w') as f:
        json.dump(api_response['response'], f)



# Testing statements
    #print(json.dumps(api_response, indent=4, sort_keys=True))
    #print(api_response)
    #print(type(api_response['response'][0]))
    #for resp in api_response['response']:
    #    for key, value in resp.items():
    #        print(f'Key: {key}\nValue: {value}\n')
    #params = {
    #    'api_key': 'e5583e21-7f08-4c36-a75b-288bf856f971',
    #    'params1': 'value1'
    #}
    #method = 'ping'
    #api_result = requests.get(api_base+method, params)
