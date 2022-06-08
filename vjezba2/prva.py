#!C:\Python310\python.exe
import base


print("")
base.start_html()
print('''
<h2>Unesite podatke:</h2>
<form action="druga.py" method="post">
  Ime:
  <input type="text" name="ime" value="">
  <br><br>
  Lozinka:
  <input type="password" name="lozinka">
  <br><br>
  Ponovi lozinku:
  <input type="password" name="rlozinka">
  <br><br>
  <input type="submit" value="Next">
</form> 
''')

base.finish_html()