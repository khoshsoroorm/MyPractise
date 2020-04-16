def checker(n):
    i = 1
    my_list = []
    # my_dict = {}
    # while i <=n:
    #     s = input()
    #     s = s.strip().split()
    #     my_dict[s[0]]= [s[1::]]
    #     i+=1
    my_dict = {'man': ['I', 'je', 'ich'], 'kheili': ['very', 'très', 'sehr'], 'alaghemand': ['interested', 'intéressé', 'interessiert'], 'barnamenevisi': ['programming', 'laprogrammation', 'Programmierung']}
    # text = input()
    text = 'I am very interested in programming'
    text = text.strip().split()
    print(text)
    t =list(my_dict.values())
    print(t[0])
    for k in my_dict:
        for v in my_dict[k]:
                if v in text:
                    print(k)


    # for i in range(len(text)):
    #     for key, value in my_dict.items():
    #
    #         # print('this is i', i, '\n this is key', key, '\n this is value', value, '\n this is text[i]', text[i])
    #         if text[i] in value:
    #             print(key)
    #         elif text[i] not in value:
    #             print(text[i])




#n = int(input())
n = 4
checker(n)