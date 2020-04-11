def team_score(s):
    my_dict = {
        'Spain': {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        'Iran': {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        'Portugal': {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        'Morocco': {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
    }
    for i in range(0, len(s)):
        if i == 0:
            if int(s[i][0]) > int(s[i][2]):
                my_dict['Iran']['wins'] += 1
                my_dict['Iran']['points'] += 3
                my_dict['Iran']['goal difference'] += int(s[i][0])
                my_dict['Spain']['loses'] += 1
                my_dict['Spain']['goal difference'] += int(s[i][2])

            if int(s[i][0]) < int(s[i][2]):
                my_dict['Spain']['wins'] += 1
                my_dict['Spain']['points'] += 3
                my_dict['Iran']['goal difference'] += int(s[i][0])
                my_dict['Iran']['loses'] += 1
                my_dict['Spain']['goal difference'] += int(s[i][2])

            else:
                my_dict['Spain']['draws'] += 1
                my_dict['Spain']['points'] += 1
                my_dict['Iran']['points'] += 1
                my_dict['Iran']['goal difference'] += int(s[i][0])
                my_dict['Iran']['draws'] += 1
                my_dict['Spain']['goal difference'] += int(s[i][2])

        if i == 1:
            if int(s[i][0]) > int(s[i][2]):
                my_dict['Iran']['wins'] += 1
                my_dict['Iran']['points'] += 3
                my_dict['Iran']['goal difference'] += int(s[i][0])
                my_dict['Spain']['loses'] += 1
                my_dict['Spain']['goal difference'] += int(s[i][2])

            if int(s[i][0]) < int(s[i][2]):
                my_dict['Spain']['wins'] += 1
                my_dict['Spain']['points'] += 3
                my_dict['Iran']['goal difference'] += int(s[i][0])
                my_dict['Iran']['loses'] += 1
                my_dict['Spain']['goal difference'] += int(s[i][2])

            else:
                my_dict['Spain']['draws'] += 1
                my_dict['Spain']['points'] += 1
                my_dict['Iran']['points'] += 1
                avg =(my_dict['Iran']['goal difference'] +
                      my_dict['Spain']['goal difference'] +
                      my_dict['Portugal']['goal difference'] +
                      my_dict['Morocco']['goal difference']) / 4
                if avg > int(s[i][0]):
                    m = avg - int(s[i][0])
                    my_dict['Iran']['goal difference'] += m
                if avg < int(s[i][0]):
                    m = avg - int(s[i][0])
                    my_dict['Iran']['goal difference'] += m

                my_dict['Iran']['draws'] += 1
                my_dict['Spain']['goal difference'] += int(s[i][2])

                print(my_dict)


my_list = ['2-2', '2-1']
# for i in range(0,2):
#    s = input()
#    my_list.append(s)

team_score(my_list)

