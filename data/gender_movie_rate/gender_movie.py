import json

users_data = open('users.json', 'r', encoding='utf-8')
users_json = json.load(users_data)

rate_data = open('rate.json', 'r', encoding='utf-8')
rate_json = json.load(rate_data)

# for user in users_json:
#     user['results'] = []

# print(users_json)

users_F = []
users_M = []

for user in users_json:
    if user['gender'] == 'M':
        users_M += [user['id']]
    else:
        users_F += [user['id']]

# print(len(users_M))
# print(len(users_F))

# movies_F = [{
#     'movie_id': 0,
#     'movie_rate_avg': 0,
#     'movie_rate_total': 0,
#     'movie_count': 0,
#     }]

# # print(users_F)

# for user_F in users_F:
#     # print(user_F)
#     for rate in rate_json:
#         if user_F == rate['user_id']:
#             # print(user_F)
#             # print(rate['user_id'])
#             flag = 0
#             for movie in movies_F:
#                 if int(rate['movie_id']) == movie['movie_id']:
#                     movie['movie_rate_total'] += int(rate['rate'])
#                     movie['movie_count'] += 1
#                     movie['movie_rate_avg'] = movie['movie_rate_total'] / movie['movie_count']
#                     flag = 1
#             if flag == 0:
#                 movies_F += [{
#                     'movie_id': int(rate['movie_id']),
#                     'movie_rate_avg': int(rate['rate']),
#                     'movie_rate_total': int(rate['rate']),
#                     'movie_count': 1,
#                 }]
#             else:
#                 flag = 0

# avg_cnt = 0      
# for movie in movies_F:
#     avg_cnt += movie['movie_count']
# avg_cnt //= len(movies_F)
# # print(avg_cnt)

# for i in range(len(movies_F)):
#     if movies_F[i]['movie_count'] < avg_cnt:
#         movies_F[i]['movie_rate_avg'] = 0

# movies_F = sorted(movies_F, key=lambda k: -k['movie_rate_avg'])[:20]

# print(movies_F)



movies_M = [{
    'movie_id': 0,
    'movie_rate_avg': 0,
    'movie_rate_total': 0,
    'movie_count': 0,
    }]

for user_M in users_M:
    for rate in rate_json:
        if user_M == rate['user_id']:
            flag = 0
            for movie in movies_M:
                if int(rate['movie_id']) == movie['movie_id']:
                    movie['movie_rate_total'] += int(rate['rate'])
                    movie['movie_count'] += 1
                    movie['movie_rate_avg'] = movie['movie_rate_total'] / movie['movie_count']
                    flag = 1
            if flag == 0:
                movies_M += [{
                    'movie_id': int(rate['movie_id']),
                    'movie_rate_avg': int(rate['rate']),
                    'movie_rate_total': int(rate['rate']),
                    'movie_count': 1,
                }]
            else:
                flag = 0
            # print(movie)

avg_cnt = 0      
for movie in movies_M:
    avg_cnt += movie['movie_count']
avg_cnt //= len(movies_M)
# print(avg_cnt)

for i in range(len(movies_M)):
    if movies_M[i]['movie_count'] < avg_cnt:
        movies_M[i]['movie_rate_avg'] = 0

movies_M = sorted(movies_M, key=lambda k: -k['movie_rate_avg'])[:20]

print(movies_M)