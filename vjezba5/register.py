#!C:\Python310\python.exe

from cmath import log
import base
import db
import cgi, os
import authentication
import cgitb

registration_error = "Registration Error!"
cgitb.enable(display=0,logdir="")

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    password = params.getvalue("password")
    password_repeat = params.getvalue("password_repeat")
    email = params.getvalue("email")

    validation_error = False
    success = False

    if password != password_repeat:
        registration_error += "<br>Passwords must match!"
        validation_error = True

    if db.get_user_by_email(email) != None:
        registration_error += "<br>Email " + email + "already exists!"
        validation_error = True

    if validation_error == False:
        success = authentication.register(username, password, email)
        if success:
            print('Location: login.py')
            
print("")
base.start_html()
print ('''
        <form method="POST">
            username <input type="text" name="username" required /><br>
            password <input type="password" name="password" required/><br>
            repeat password <input type="password" name="password_repeat" required/><br>
            email <input type="email" name="email" required/><br>
            
            <input type="submit" value="Register"/>
        </form>
''')

print("<a href=index.py>Home</a>")
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>" + registration_error + "</div>")
base.finish_html()
