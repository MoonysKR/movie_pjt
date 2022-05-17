import sys

sys.stdin = open('ratings.dat', encoding='ISO-8859-1')

data = []

lst = []

for i in range(1000209):
    info = input()
    user_id = info.split('::')[0]
    movie_id = info.split('::')[1]
    ratings = info.split('::')[2]
    dic = {
        'id': user_id,
        'results': [
            {
                'movie_id': movie_id,
                'ratings': ratings,
            }
        ]

    }
    
    if user_id in lst:
        for dat in data:
            if dat['id'] == user_id:
                dat['results'] += dic['results']
    else:
        lst += dic['id']
        data += [dic]
            
    print(data)
    
# print(data)

# import json

# with open('ratings.json', 'w') as f:
#     json_string = json.dump(data, f, indent=2)