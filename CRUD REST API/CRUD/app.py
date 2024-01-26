import requests
import json 

url = "http://127.0.0.1:8000/student/"


def get_data(id=None):
	data = {}
	if id is not None:
		data = {'id':id}
	json_data = json.dumps(data)
	r = requests.get(url=url,data=json_data)
	data = r.json()
	print(data)



def create_data(name,email,password):
	data = {
		'name':name,
		'email':email,
		'password':password,
	}
	headers={'content-type':'application/json'}
	json_data = json.dumps(data)
	r = requests.post(data=json_data,url=url,headers=headers)
	data = r.json()
	print(data)

def update_data():
	data = {
		'id':4,
		'name':'Sohan',
		'email':'sohan@gmail.com',
		'password':'sohan123',
	}
	headers={'content-type':'application/json'}
	json_data = json.dumps(data)
	
	r = requests.put(data=json_data,url=url,headers=headers)
	data = r.json()
	print(data)




def delete_data(id):
	data = {'id':id}
	headers={'content-type':'application/json'}
	json_data = json.dumps(data)
	r = requests.delete(data=json_data,url=url,headers=headers)
	data = r.json()
	print(data)
   


	

# CRUD OPERATIONS 
	
# C : Create 
	
create_data(name='mohit',email='mohit@gmail.com',password='mohit123')

# R : Read

get_data()    # view all data

get_data(id=3)    # view data which id=3

# U : Update 

update_data()    

# D : Delete

delete_data(id=2)