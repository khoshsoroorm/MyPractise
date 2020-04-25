import mysql.connector

my_lsit = []
out = []
c = mysql.connector.connect(user='root', password='', database='learn_mysql', host='127.0.0.1')

cursor = c.cursor()
query = 'SELECT * FROM employee'
cursor.execute(query)
temp = None
N = 1

for lines in cursor:
    my_lsit.append(list(lines))
    my_lsit.sort(key=lambda x: x[2], reverse=True)

for i in range(0, len(my_lsit) - 1):
    if my_lsit[i][2] == my_lsit[i + 1][2]:
        if my_lsit[i][1] > my_lsit[i + 1][1]:
            temp = my_lsit[i][1]
            my_lsit[i][1] = my_lsit[i + 1][1]
            my_lsit[i + 1][1] = temp

for name, weight, height in my_lsit:
    print(name, weight, height)

c.close()
