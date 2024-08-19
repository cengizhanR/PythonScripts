import pickle
# friends1 = {"Dan":[20,"London",3234342], "dddddd":[25,"ada",43525222]}
# friends2 = {"Dada":[20,"London",3234342], "ada":[25,"Madrid",43525222]}
# friends = (friends1, friends2)
# # with open('friends.txt','w') as f:
# #     f.write(friends)
#
# with open ('friends.dat','wb') as f:
#     pickle.dump(friends,f)
#
# with open('friends.dat', 'rb') as f:
#     obj=pickle.load(f)
#     print(type(obj))
#     print(obj)
####3JSON
import json
# friends = {"Dan":[20,"London",3234342], "dddddd":[25,"ada",43525222], 4: list({1,2})}
#
# with open('friends.json','w') as f:
#     json.dump(friends,f, indent=4)
#
# json_string=json.dumps(friends,indent=4)
# print(json_string)
# with open('friends.json', 'rt') as f:
#     obj = json.load(f)
#     print(type(obj))
#     print(obj)
#
# json_string = """{
#     "Dan": [
#         20,
#         "London",
#         3234342
#     ],
#     "dddddd": [
#         25,
#         "ada",
#         43525222
#     ]
# }"""
# obj = json.loads(json_string)
# print(type(obj))
# print(obj)
import requests
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# print(type(todos))
# print(todos)
# for task in todos:
#     if task['completed'] == True:
#         print(task)

# def serialize(object,file,protocol):
#     if protocol == 'json':
#         import json
#         with open(file,'w') as f:
#             json.dump(object,f, indent=4)
#     elif  protocol == 'pickle':
#         import pickle
#         with open (file,'wb') as f:
#              pickle.dump(object,f)
#     else:
#         print('Invalid serialization. Use pickle or json!')
#
#
# def deserialize(file,protocol):
#     if protocol == 'json':
#         import json
#         with open(file, 'rt') as f:
#             obj = json.load(f)
#             return obj
#     elif  protocol == 'pickle':
#         import pickle
#         with open(file, 'rb') as f:
#             obj=pickle.load(f)
#             return obj
#     else:
#         print('Invalid serialization. Use pickle or json!')
#
# d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}
#
# # Serializing using pickle
# serialize(d1, 'a.dat', 'pickle')
# myDict = deserialize('a.dat', 'pickle')
# print(f'pickle: {myDict}')
#
# # serializing using pickle
# serialize(d1, 'a.json', 'json')
#
# # deserializing
# x = deserialize('a.json', 'json')
# # Notice how the tuple value was not preserved!
# print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}
import json
# import requests
# import csv
# response = requests.get('https://jsonplaceholder.typicode.com/users')
# users = response.json()
# print(type(users))
# print(users)
# with open('users.csv', 'w') as f:
#     writer = csv.writer(f)
#
#     # write a header to file
#     writer.writerow(("Name", "City", "GPS", "Company"))
#
#     for user in users:
#         # getting the data from the dictionary
#         name = user['name']
#         #print(name)
#         city = user['address']['city']
#         #print(city)
#         lat = user['address']['geo']['lat']
#         lng = user['address']['geo']['lng']
#         # constructing the GPS coordinates in form of (lat, lng)
#         geo = f'({lat},{lng})'
#         company_name = user['company']['name']
#         csv_data = (name, city, geo, company_name)
#         writer.writerow(csv_data)