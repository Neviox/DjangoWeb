#!python.exe

import os
import subjects
import cgi
from http import cookies

params=cgi.FieldStorage()
cookie=cookies.SimpleCookie()

cookies_string = os.environ.get('HTTP_COOKIE', '')
cookie_obj=cookies.SimpleCookie(cookies_string)


for i in params:
    cookie[i]=params.getvalue(i)
    print (cookie.output())


print("""
<!DOCTYPE HTML>
<html>
<style>
table, td, th{
    border: 1px solid blue;
}
</style>
<body>
<table>
<form>

    <tr>
        """)

for i in subjects.subjects.values():
    print("""   
    <tr>
        <th>""")
    print(i["name"])
    print("""
        </th>
        <th>
""")
    print('<input type="submit" name="'+i["name"].replace(" ", "+")+'" value="'+i["name"]+'">')

    print("""
        </th>
    </tr>
    """)

print("""
</table>

    """)



print("""

""")

print("""
</form>
<body>
</html>

""")

for i in cookie_obj:
    print(cookie_obj[i].value)