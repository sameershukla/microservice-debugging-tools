import requests
import json
import pandas as pd
from matplotlib import pyplot as plt

response = requests.get('http://localhost:8082/actuator/httptrace')
json = json.dumps(response.json())
df = pd.read_json(json, orient='columns')

for data in df.items():
    okList = []
    notFoundList = []
    getList = []
    postList = []
    for d in data[1]:
        status = d['response']['status']
        method = d['request']['method']
        uri = d['request']['uri']
        if (status == 200 and 'actuator' not in uri):
            okList.append(status)
        if (status == 404 and 'actuator' not in uri):
            notFoundList.append(status)
        if (method == 'GET' and 'actuator' not in uri):
            getList.append(method)
        if (method == 'POST' and 'actuator' not in uri):
            postList.append(method)

print('Successful Count:', len(okList))
print('Not Found List:', len(notFoundList))

print('GET Count:', len(getList))
print('POST List:', len(postList))