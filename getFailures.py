import requests
import json

client = requests.session()

headers = {
    "Authorization": "bearer %s" % "",
    "Content-Type": "application/json"
}

data = {}

HOST = "https://api.surveymonkey.net"
SURVEY_LIST_ENDPOINT = "/v3/surveys/171070012/responses/bulk"

uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)

response = client.get(uri, headers=headers)

response_json = response.json()
# survey_list = response_json["data"]["surveys"]

print(response_json['data'])
total = response_json['total']
# failure_array = []

for i in range(0, total):
    if response_json['data'][i]['quiz_results']['incorrect'] > 0:
        print(response_json['data'][i]['metadata']['contact']['email']['value'])
