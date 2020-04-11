import operator

def fave(n):
    my = {}
    my_list = []
    for i in range(1, n + 1):
        m = input()
        m = m.lower().strip().split()
        for i in range(1,len(m)):

            my_list.append(m[i])
    for item in my_list:
        if item != my:
            my[item] = my_list.count(item)
    my_value = my.values()
    my_keys = my.keys()
    final_dict = {}
# ta inja faqat monde sort kardan dictionary


    return my


print(fave(4))
