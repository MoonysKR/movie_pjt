import json

users_data = open('users.json', 'r', encoding='utf-8')
users_json = json.load(users_data)

rate_data = open('rate.json', 'r', encoding='utf-8')
rate_json = json.load(rate_data)

# for user in users_json:
#     user['results'] = []

# print(users_json)

	# *  1:  "Under 18"
	# * 18:  "18-24"
	# * 25:  "25-34"
	# * 35:  "35-44"
	# * 45:  "45-49"
	# * 50:  "50-55"
	# * 56:  "56+"

users_0 = []
users_1 = []
users_2 = []
users_3 = []
users_4 = []
users_5 = []
users_6 = []



for user in users_json:
    if user['age'] == '1':
        users_0 += [user['id']]
    elif user['age'] == '18':
        users_1 += [user['id']]
    elif user['age'] == '25':
        users_2 += [user['id']]
    elif user['age'] == '35':
        users_3 += [user['id']]
    elif user['age'] == '45':
        users_4 += [user['id']]
    elif user['age'] == '50':
        users_5 += [user['id']]
    elif user['age'] == '56':
        users_6 += [user['id']]



for i in range(0, 7):
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

    with open(f'age_{i}.json', 'w') as f:   
        json_string = json.dump(globals()['movies_{}'.format(i)], f, indent=2)