#!C:\Python310\python.exe
import base
import os,cgi
import session
import authentication
import cgitb

cgitb.enable(display=0,logdir="")

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    success, user_id = authentication.authenticate(username, password)
    if success:
        session_id = session.create_session()
        session.add_to_session({"user_id": user_id}, session_id=session_id)
        print ('Location: index.py')

print("")
base.start_html()
print ('''<form method="POST">
username <input type="text" name="username" />
password <input type="password" name="password"/>
<input type="submit" value="Login"/>
</form>''')
print("<a href=index.py>Home</a> <br>")
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print ("<div>Login Error</div>")
base.finish_html()