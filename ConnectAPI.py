
import requests

import json

import e_certifi




url = "link of otdsws rest authentication credentials"




payload = json.dumps({

  "userName": "",

  "password": ""

})




headers = {

  'Content-Type': 'application/json'

}





response_OTDS = requests.request("POST", url, headers=headers, data=payload, verify=e_certifi.where())




print(response_OTDS.text)




OTDS_token = response_OTDS.json()['ticket']

OTDS_token




# Set the base URL for the OpenText Content Server REST API

base_url = ''




# Set the endpoint for the search

search_endpoint = '/search'




# Set the headers for the request

headers = {

  'OTDSTicket': OTDS_token,

  'Content-Type': 'application/json'

}




# Set the payload for the search request

 


payload = {

    'where': 'OTName:' + 'payload of search request' 
}



# Send the POST request to search for node IDs

response = requests.post(url = base_url+search_endpoint, headers=headers, data=payload, verify = e_certifi.where())

search_results = response.json()


s1 = search_results['results'][0]['data']['properties']['id']

s2 = search_results['results'][0]['data']['properties']['parent_id']


search_results_together = [s1, s2]

search_results_together