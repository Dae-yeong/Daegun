#!python


import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

#Redirection: 페이지 주소 설정
print("Location: index.py?id="+title)
print()
