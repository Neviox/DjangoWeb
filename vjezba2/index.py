#!C:\Python310\python.exe
import cgi
import base


params = cgi.FieldStorage()
ime = params.getvalue("ime")
lozinka = params.getvalue("lozinka")
status = params.getvalue("status")
email = params.getvalue("email")
smjer =params.getvalue("smjer")
zavrsni = params.getvalue("zavrsni")
napomena= params.getvalue("napomena")

if(zavrsni is None):
    zavrsni="Ne"

print("")
base.start_html()
print ('''
<h2>Uneseni podaci:</h2>    
''')
print("Ime:  ")
print(ime)
print("<br><br>")
print("E-mail:  ")
print(email)
print("<br><br>")
print("Status:  ")
print(status)
print("<br><br>")
print("Smjer:  ")
print(smjer)
print("<br><br>")
print("Zavrsni rad:  ")
print(zavrsni)
print("<br><br>")
print("Napomena:  ")
print(napomena)

print ('''<br><br>
    <a href="prva.py">Na pocetak</a>
''')

base.finish_html()

