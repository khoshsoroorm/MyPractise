import re
regtext  = '(^[\w\d]+@\w+\.\w{2,3})'

inp_email = input()
if re.search(regtext,inp_email):
    print('OK')
else:
    print('WRONG')
