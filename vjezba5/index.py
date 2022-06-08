#!C:\Python310\python.exe

import base
import cgitb

cgitb.enable(display=0,logdir="")
print ("")
base.start_html()

print("<a href='login.py'>Login</a>")
print("<br>")
print("<a href='register.py'>Register</a>")
print("<br>")
print("<a href='logout.py'>Logout</a>")
print("<br>")
print("<a href='password_change.py'>Password change</a>")

base.finish_html()
