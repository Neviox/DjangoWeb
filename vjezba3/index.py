#!C:\Python310\python.exe

import subjects
import cgi
import cgitb
from http import cookies
import os

#cgitb.enable(display=0,logdir="")
params=cgi.FieldStorage()
cookie=cookies.SimpleCookie()
cookies_string= os.environ.get('HTTP_COOKIE','')
cookies_object= cookies.SimpleCookie(cookies_string)

print("")

def checked():
    if(cookie[i["name"].replace(" ",".")].value == subjects.status_names["not"]):
        print('<label for="'+i["name"]+'">Not Selected</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["not"]+ '"checked="checked">')

        print('<label for="' +i["name"]+ '">Enrolled</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["enr"]+ '">')

        print('<label for="' +i["name"]+ '">Passed</label>')
        print('<input type="radio" '+' id="' +i["name"]+ '" name="' +i["name"]+ '" value="' +subjects.status_names["pass"]+ '">')

    elif(cookie[i["name"].replace(" ",".")].value == subjects.status_names["enr"]):
        print('<label for="'+i["name"]+'">Not Selected</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["not"]+ '">')

        print('<label for="' +i["name"]+ '">Enrolled</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["enr"]+ '"checked="checked">')

        print('<label for="' +i["name"]+ '">Passed</label>')
        print('<input type="radio" '+' id="' +i["name"]+ '" name="' +i["name"]+ '" value="' +subjects.status_names["pass"]+ '">')

    elif(cookie[i["name"].replace(" ",".")].value == subjects.status_names["pass"]):
        print('<label for="'+i["name"]+'">Not Selected</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["not"]+ '">')

        print('<label for="' +i["name"]+ '">Enrolled</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["enr"]+ '">')

        print('<label for="' +i["name"]+ '">Passed</label>')
        print('<input type="radio" '+' id="' +i["name"]+ '" name="' +i["name"]+ '" value="' +subjects.status_names["pass"]+ '"checked="checked">')

    else:
        print('<label for="'+i["name"]+'">Not Selected</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["not"]+ '">')

        print('<label for="' +i["name"]+ '">Enrolled</label>')
        print('<input type="radio" '+' id="' +i["name"]+'" name="' +i["name"]+ '" value="' +subjects.status_names["enr"]+ '"checked="checked">')

        print('<label for="' +i["name"]+ '">Passed</label>')
        print('<input type="radio" '+' id="' +i["name"]+ '" name="' +i["name"]+ '" value="' +subjects.status_names["pass"]+ '">')



if not cookies_string:
    for i in subjects.subjects.values():
        cookie[i["name"].replace(" ",".")] = subjects.status_names["not"]
else:
    for i in subjects.subjects.values():
        coke=cookies.SimpleCookie()
        coke.load(cookies_string)
        if not params.getvalue(i["name"]):
            cookie[i["name"].replace(" ",".")] = coke[i["name"].replace(" ",".")].value
        else:
            cookie[i["name"].replace(" ",".")] = params.getvalue(i["name"])

print(cookie.output())


if not params.getvalue("godina"):
    godina = "1st Year"
else:
    godina=params.getvalue("godina")

if godina!= "Upisni List":

    print("""<!DOCTYPE html>
    <html>
    <style>
    table, th, td {
    border:0.5px solid black;
    }
    </style>
    <body>
    <h2>Forma</h2>
    <form>
    <table>

            <tr>
                <th>""")

    print(godina)

    print  ("""
                </th>
                <th>
                    ECTS:
                </th>
                <th>
                    Status:
                </th>
            </tr>
    """)
    for i in subjects.subjects.values():
        if (i["year"] == subjects.year_ids[godina]):
            print("""
                <tr>
                    <th>
            """)

            print(i["name"])
            print("""
                    </th>
                    <th>
            """)

            
            print(i["ects"])
            print("""
                    </th>
                    <th>
            """)
            
            checked()
            
            print("""
                    </th>
                </tr>
            """)

    print("""
        </table>
        <input name=godina type="submit" value="1st Year">
        <input name=godina type="submit" value="2nd Year">
        <input name=godina type="submit" value="3rd Year">
        <input name=godina type="submit" value="Upisni List">
    </form>
    </body>
    </html>""")
    
else:
    print  ("""
    <!DOCTYPE html>
    <html>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    <body>
        <table>
            <tr>
                <th>""")
    print("Predmeti")  
    print("""</th>
          <th>Status</th> 
          <th>Ects</th>
      </tr>""")

    for i in subjects.subjects.values():
        print("""   
            <tr>
            <th>""")
        print(i["name"])
        print("""
        </th>
            <th>""")

        print(cookie[i["name"].replace(" ", ".")].value)
        print("""
        </th>
            <th>""")    

        print(i["ects"])
        print("""</th>
            </tr>""")
            
    print("""            
            </table>
            <a href="http://localhost/cgi-bin/vjezba3/index.py">Go back</a>
    </form>""")
    print(""" 
    </body>
    </html>""")
        

                
