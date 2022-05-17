import sys

sys.stdin = open('users.dat', encoding='ISO-8859-1')

data = []

for i in range(6040):
    info = input()
    id = info.split('::')[0]
    gender = info.split('::')[1]
    age = info.split('::')[2]
    occupation = info.split('::')[3]
    
    user = {
        'id': id,
        'gender': gender,
        'age': age,
        'occupation': occupation
    }

    data += [user]

import json

with open('users.json', 'w') as f:
    json_string = json.dump(data, f, indent=2)