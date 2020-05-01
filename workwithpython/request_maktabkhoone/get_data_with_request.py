import requests
from bs4 import BeautifulSoup
import re

# get request from the maktabkhoone.org
req = requests.get('https://maktabkhooneh.org/learn/?q=%D9%85%DA%A9%D8%AA%D8%A8+%D9%BE%D9%84%D8%A7%D8%B3')
# check if request is OK print 200
# print(req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')
# finde div for seach
res = soup.find_all('a', class_='course-card__wrapper')
# set my div for regex
rex_text = '<div class="course-card__badge-text">(\s*\n*مکتب\s*\n*\s*.*\n*\s*)</div>?'
name_course = '<div class="course-card__title">(.*)</div>'
count = 0
for item in res:
    if re.search(rex_text, str(item)):
        name = re.search(name_course,str(item))
        print(name[1])
        #count += 1

#print('', count)
