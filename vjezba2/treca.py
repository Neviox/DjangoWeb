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

print("")
base.start_html()

print ('''
 <h2>Unesite podatke:</h2>
    <form action="index.py" method="post">
    Napomena: <input type="text" name="napomena">
    <br><br>''')
print ('<input type="hidden" name="ime" value="''' + ime + '">')
print ('<input type="hidden" name="lozinka" value="' + lozinka + '">')
print ('<input type="hidden" name="status" value="''' + status + '">')
print ('<input type="hidden" name="email" value="' + email + '">')
print ('<input type="hidden" name="smjer" value="''' + smjer + '">')
print ('<input type="hidden" name="zavrsni" value="' + zavrsni + '">')
print ('''<input type="submit" value="Next">
</form>
''')

base.finish_html()