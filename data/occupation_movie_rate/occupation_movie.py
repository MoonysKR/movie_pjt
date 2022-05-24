import json

users_data = open('users.json', 'r', encoding='utf-8')
users_json = json.load(users_data)

rate_data = open('rate.json', 'r', encoding='utf-8')
rate_json = json.load(rate_data)

# for user in users_json:
#     user['results'] = []

# print(users_json)

users_0 = []
users_1 = []
users_2 = []
users_3 = []
users_4 = []
users_5 = []
users_6 = []
users_7 = []
users_8 = []
users_9 = []
users_10 = []
users_11 = []
users_12 = []
users_13 = []
users_14 = []
users_15 = []
users_16 = []
users_17 = []
users_18 = []
users_19 = []
users_20 = []

for user in users_json:
    if user['occupation'] == '0':
        users_0 += [user['id']]
    elif user['occupation'] == '1':
        users_1 += [user['id']]
    elif user['occupation'] == '2':
        users_2 += [user['id']]
    elif user['occupation'] == '3':
        users_3 += [user['id']]
    elif user['occupation'] == '4':
        users_4 += [user['id']]
    elif user['occupation'] == '5':
        users_5 += [user['id']]
    elif user['occupation'] == '6':
        users_6 += [user['id']]
    elif user['occupation'] == '7':
        users_7 += [user['id']]
    elif user['occupation'] == '8':
        users_8 += [user['id']]
    elif user['occupation'] == '9':
        users_9 += [user['id']]
    elif user['occupation'] == '10':
        users_10 += [user['id']]
    elif user['occupation'] == '11':
        users_11 += [user['id']]
    elif user['occupation'] == '12':
        users_12 += [user['id']]
    elif user['occupation'] == '13':
        users_13 += [user['id']]
    elif user['occupation'] == '14':
        users_14 += [user['id']]
    elif user['occupation'] == '15':
        users_15 += [user['id']]
    elif user['occupation'] == '16':
        users_16 += [user['id']]
    elif user['occupation'] == '17':
        users_17 += [user['id']]
    elif user['occupation'] == '18':
        users_18 += [user['id']]
    elif user['occupation'] == '19':
        users_19 += [user['id']]
    elif user['occupation'] == '20':
        users_20 += [user['id']]


for i in range(0, 1):
    globals()['movies_{}'.format(i)] = [{
        'movie_id': 0,
        'movie_rate_avg': 0,
        'movie_rate_total': 0,
        'movie_count': 0,
        }]

    for user in globals()['users_{}'.format(i)]:
        for rate in rate_json:
            if user == rate['user_id']:
                flag = 0
                for movie in globals()['movies_{}'.format(i)]:
                    if int(rate['movie_id']) == movie['movie_id']:
                        movie['movie_rate_total'] += int(rate['rate'])
                        movie['movie_count'] += 1
                        movie['movie_rate_avg'] = movie['movie_rate_total'] / movie['movie_count']
                        flag = 1
                if flag == 0:
                    globals()['movies_{}'.format(i)] += [{
                        'movie_id': int(rate['movie_id']),
                        'movie_rate_avg': int(rate['rate']),
                        'movie_rate_total': int(rate['rate']),
                        'movie_count': 1,
                    }]
                else:
                    flag = 0
                # print(globals()['movies_{}'.format(i)])

    avg_cnt = 0      
    for movie in globals()['movies_{}'.format(i)]:
        avg_cnt += movie['movie_count']
    avg_cnt //= len(globals()['movies_{}'.format(i)])
    # print(avg_cnt)

    for j in range(len(globals()['movies_{}'.format(i)])):
        if globals()['movies_{}'.format(i)][j]['movie_count'] < avg_cnt:
            globals()['movies_{}'.format(i)][j]['movie_rate_avg'] = 0

    globals()['movies_{}'.format(i)] = sorted(globals()['movies_{}'.format(i)], key=lambda k: -k['movie_rate_avg'])[:20]

    with open(f'occupation_{i}.json', 'w') as f:   
        json_string = json.dump(globals()['movies_{}'.format(i)], f, indent=2)