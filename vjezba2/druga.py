#!C:\Python310\python.exe
import cgi
import base


params=cgi.FieldStorage()
ime=params.getvalue("ime")
lozinka=params.getvalue("lozinka")
rlozinka=params.getvalue("rlozinka")

if rlozinka!=lozinka:
    print("Location: prva.py")
    
print("")
base.start_html()

print('''
<h2>Unesite podatke:</h2>

<form action="treca.py" method="post">
  Status:
  <input type="radio" name="status" value="redovni"> Redovni
  <input type="radio" name="status" value="izvanredni"> Izvanredni
  <br><br>
  E-mail: <input type="email" name="email">
  <br><br>
  <select name="smjer">
    <option value="programiranje">Programiranje</option>
    <option value="baze_podataka">Baze podataka</option>
    <option value="mreze">Mreze</option>
    <option value="informacijski_sustavi">Informacijski sustavi</option>
  </select>
  <br><br>
  <input type="checkbox" name="zavrsni" value="Da"> Zavrsni<br>
  ''')
print ('<input type="hidden" name="ime" value="' + ime + '">')
print ('<input type="hidden" name="lozinka" value="' + lozinka + '">')
print ('''
<br>
<input type="submit" value="Next">
</form>
''')
base.finish_html()