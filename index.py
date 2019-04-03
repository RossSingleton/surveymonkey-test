import requests
import json

client = requests.session()

headers = {
    "Authorization": "bearer %s" % "",
    "Content-Type": "application/json"
}

data = {}

HOST = "https://api.surveymonkey.net"
SURVEY_LIST_ENDPOINT = "/v3/surveys"

uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)

response = client.get(uri, headers=headers)

response_json = response.json()
# survey_list = response_json["data"]["surveys"]

print(response_json)
