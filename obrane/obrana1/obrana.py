#! python.exe

from pdb import post_mortem
import subjects
import cgi
from http import cookies
import os

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE','')
cookie.load(cookie_string)

if params:
    for i in params:
#        if cookie[i].value == "dodan":
#            postoji = 1
#        else:
            cookie[i] = "dodan"

print(cookie.output())

print("""
    <!DOCTYPE HTML>
        <html>
            <body>
                <form action="obrana.py" method="post">
                    <table>""")
for i in subjects.subjects.values():
    print("""
                        <tr>
                            <th>""")
    print(i["name"])
    print("""</th>
            <th>
            <input type="submit" name=""")
    print(i["name"].replace(" ","+"))
    print(""" " value="Add to cookie">
            </th>
                        </tr>""")


for i in cookie:
    print("""
                        <tr>
                            <th>""")
    print(i.replace("+"," "))
    print("""</th>
                        </tr>
                        """)

    print("""
      </table>
                </form>


                
            </body>
        </html>""")



cookiee = cookies.SimpleCookie()
cookiee.load(cookie_string)


for i in params:
    if not cookiee[i]:
        print("ne_postoji")
    else:
        print("("+i+"vec postoji)")

