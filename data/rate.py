import sys
import random

sys.stdin = open('ratings.dat', encoding='ISO-8859-1')

data = []
lst = []

for i in range(1000209):
    info = input()
    user_id = info.split('::')[0]
    movie_id = info.split('::')[1]
    rate = info.split('::')[2]
    dic = {
        'user_id': user_id,
        'movie_id': movie_id,
        'rate': rate
    }

    data += [dic]

    # 표본 추출
#     lst += [dic]

# new_lst = random.sample(lst, 100000)
# print(new_lst)

# for i in range(100000):
#     dic = new_lst[i]
#     data += [dic]

# print(data)

import json

with open('rate.json', 'w') as f:
    json_string = json.dump(data, f, indent=2)