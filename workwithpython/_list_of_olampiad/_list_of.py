def _list_of_olampiad(n):
    my_list = []
    for i in range(0, n):
        s = input()
        s = s.lower()
        my_list.append(s.strip().split('.'))
    my_list = sorted(my_list)
    return my_list



n = int(input())

for char in _list_of_olampiad(n):
        if char[0]=='f':
            print(char[0], char[1].capitalize(), char[2])
        if char[0]=='m':
            print(char[0], char[1].capitalize(), char[2])
