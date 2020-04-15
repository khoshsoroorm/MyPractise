def checker(s):
    my_string2 = 0
    ss = s.replace('.', '')
    my_line = ss.strip().split()
    my_string = s.strip().split('.')
    for l in range(len(my_string)):
        char = my_string[l].split()
        for i in range(1, len(char)):
            if char[i].istitle():
                print(char[i], my_line.index(char[i]) + 1)
                h = my_line.index(char[i])
                my_line[h] = 1
                my_string2 += 1
    if my_string2 == 0:
        print(None)


m = input()
# m = '''The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.'''
checker(m)
