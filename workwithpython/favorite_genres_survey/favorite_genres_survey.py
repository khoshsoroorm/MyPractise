import operator


def fave(n):
    my = {}
    my_list = []
    for i in range(1, n + 1):
        m = input()
        m = m.lower().strip().split()
        for i in range(1, len(m)):
            my_list.append(m[i])
    for item in my_list:
        if item != my:
            my[item] = my_list.count(item)
    output_dict = {}
    for key in sorted(my.keys()):
        output_dict[key] = my[key]

    sorted_d = dict(sorted(output_dict.items(), key=operator.itemgetter(1), reverse=True))
    ddd = {'horror': 0, 'romance': 0, 'comedy': 0, 'history': 0, 'adventure': 0, 'action': 0}
    for item in ddd:
        if item not in sorted_d:
            sorted_d[item] = 0

    for item in sorted_d:
        print(item.title(), ':', sorted_d[item])


n = int(input())


fave(n)
