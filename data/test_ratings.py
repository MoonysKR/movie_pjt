import sys
import random

sys.stdin = open('ratings.dat', encoding='ISO-8859-1')

data = []
lst = []
arr = []

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
    # 표본 추출
#     lst += [dic]

# new_lst = random.sample(lst, 100000)
# # print(new_lst)

# for i in range(100000):
#     dic = new_lst[i]
#     if dic['id'] in arr:
#         for dat in data:
#             if dat['id'] == dic['id']:
#                 dat['results'] += dic['results']
#     else:
#         arr += [dic['id']]
#         data += [dic]
    
    # print(arr)

# print(data)

    # 기존 코드
    if user_id in lst:
        for dat in data:
            if dat['id'] == user_id:
                dat['results'] += dic['results']
    else:
        lst += [dic['id']]
        data += [dic]
    
    # print(lst)
    # print(data)
    
# print(data)

import json

with open('ratings.json', 'w') as f:
    json_string = json.dump(data, f, indent=2)