import requests 
import json 


url = 'http://127.0.0.1:8000/create-student/'

data = {
    'name':'raj',
    'email':'raj@gmail.com',
    'password':'raj123',
}

json_data = json.dumps(data)
r = requests.post(url=url,data=json_data)
data = r.json()
print(data)   