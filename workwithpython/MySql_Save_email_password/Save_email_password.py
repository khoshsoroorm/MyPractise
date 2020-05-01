import mysql.connector
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def check(email):
    if (re.search(regex, email)):
        return True
    else:
        return False


def check_pass(password):
    x = True
    while x:
        if not re.search("[a-z]", password):
            break
        elif not re.search("[0-9]", password):
            break
        else:
            x = False
            break
    if x:
        return False
    return True


cn = mysql.connector.connect(user='root', password='Morteza2202000', database='learn_mysql', host='127.0.0.1')
cursor = cn.cursor()
insert_query = "INSERT INTO mail (email , password) values(%s,%s);"

mail_input = input('please enter your email:\n')
check1 = False
while check(mail_input) == False:
    mail_input = input('please enter a valid email:\n')
if check(mail_input):
    pass_input = input('please type password\n')
    while check_pass(pass_input) == False:
        pass_input = input('Please Enter the valid Password\n')
    if check_pass(pass_input):
        val = (mail_input, pass_input)

        cursor.execute(insert_query, val)
        cn.commit()

cn.close()
