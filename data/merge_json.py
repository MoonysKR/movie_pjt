import json

users_data = open('users.json', 'r', encoding='utf-8')
users_json = json.load(users_data)

ratings_data = open('ratings.json', 'r', encoding='utf-8')
ratings_json = json.load(ratings_data)

# for user in users_json:
#     user['results'] = []

# print(users_json)

for user in users_json:
    for rating in ratings_json:
        if user['id'] == rating['id']:
            user['results'] = rating['results']

with open('merge.json', 'w') as f:
    json_string = json.dump(users_json, f, indent=2)