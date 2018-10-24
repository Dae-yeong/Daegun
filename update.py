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
else:
    pageId = 'Welcome'
    description = 'Hello, DGH'
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
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type = "text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">
        {form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
  </body>
</html>'''.format(title=pageId, desc= description, listStr = listStr, form_default_title=pageId,
form_default_description=description))
