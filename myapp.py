import requests
import json
# URL = "http://127.0.0.1:8000/studentCreate/"

# data = {
#     'name': 'Anshu',
#     'roll': 101,
#      'city':'Ahmedabad'
# }
# json_data = json.dumps(data)
# # r = requests.get(url=URL)
# r = requests.post(url=URL, data= json_data)
# print(r)
# data = r.json()
# print(data)

URL = "http://127.0.0.1:8000/studentApi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id' : id}

    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def postData():
    data = {
       'name':'singh krishna',
        'roll': 11,
        'city': 'ranchi'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)



def updateData():
    data = {
        'id' : '4',
        'name': 'sunita',
        'city' : 'Ajamgand'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# we will delete data using id or name
def deleteData():
    data = {'id': 4}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}

    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
get_data(1)
# postData()
updateData()
deleteData()
