# with open('movies.dat', encoding='ISO-8859-1') as f:
#     contents = f.read()
#     print(contents[300])
#     movies = {}
#     pk = contents.split('::')[0]
#     title = contents.split('::')[1]
    
#     genres_tmp = contents.split('::')[2]
#     # Animation|Children's|Comedy
#     genres = []
    
#     genres += [genres_tmp.split('|')]

    
#     print(genres_tmp)

import sys

sys.stdin = open('movies.dat', encoding='ISO-8859-1')

data = []

for i in range(3883):
    info = input()
    id = info.split('::')[0]
    title = info.split('::')[1]
    genres_tmp = info.split('::')[2]
    genres = []
    for j in range(len(genres_tmp.split('|'))):
        genres += [genres_tmp.split('|')[j]]

    # print(id)
    # print(title)
    # # print(genres_tmp)
    # print(genres)
    movies = {
        'id': id,
        'title': title,
        'genres': genres
        }
    
    data += [movies]
    
# print(data)

import json

with open('data.json', 'w') as f:
    json_string = json.dump(data, f, indent=2)