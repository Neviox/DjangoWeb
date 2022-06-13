#!C:\Users\Rogulj\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import cgitb
from http import cookies
import os
import subjects

cgitb.enable(display=0,logdir="")
params = cgi.FieldStorage()
cookie = cookies.SimpleCookie()
if params:
    cookie["name"]=params.getvalue("name")
    cookie["lastName"]=params.getvalue("lastName")
    cookie["status"]=params.getvalue("status")
print(cookie)


print("""
<html>
<head></head>
<body>
<form action="./obrana.py" method="post">
Name:<input type="text" name="name" value=""><br>
Last name:<input type="text" name="lastName" value=""><br>
Redovan<input type="radio" name="status" value="redovan"><br>
Izvanredan<input type="radio" name="status" value="izvanredan"><br>
<input type="submit" value="Submit">
</form>


</body>
</html>

""")

if params:
    print(params.getvalue("name"))
    print(params.getvalue("lastName"))
    print(params.getvalue("status"))

if os.environ.get("HTTP_COOKIE"):
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie.load(cookie_string)
    print(cookie.get("name").value)
    print(cookie.get("lastName").value)
    print(cookie.get("status").value)