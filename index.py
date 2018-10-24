#!python
print("content-type: text/html; charset=euc-kr\n")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, DGH'
    update_link = ''
print('''<!doctype html>
<html>
  <head>
    <title>실질객관대건고등학교-환영합니다!</title>
    <meta charset="euc-kr">
  </head>
  <body>
    <h1><a href="index.py">대건고</a></h1>
    <ol>
    {listStr}
    </ol>
    <a href="create.py">create</a>
    {update_link}
    <h2>{title}</h2>
    <p style="margin-top:30px;">{desc}</p>
  </body>
</html>'''.format(title=pageId, desc= description, listStr = listStr, update_link = update_link))
