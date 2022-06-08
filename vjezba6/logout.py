#!C:\Python310\python.exe
from cmath import log
from http import cookies
import base, session
import cgitb

cgitb.enable(display=0,logdir="")

cookies_object = cookies.SimpleCookie()
cookies_object["session_id"] = ""
cookies_object["session_id"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
print (cookies_object.output())
session.destroy_session()
print ("Location: login.py")
print("")
base.start_html()
base.finish_html()