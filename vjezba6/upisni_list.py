#!C:\Python310\python.exe
import cgitb
import cgi
from multiprocessing import Value
import db
import session
import users_controller
import base
import random

cgitb.enable(display=0,logdir="")

params = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print ("Location: login.py")
else:
	user_id = data.get("user_id", None)
	user_role = users_controller.get_user_role(user_id)
	if user_role != "admin":
		print ("Location: index.py")
	else:
		upisni_list = params.getvalue("upisni_list")
 


print ()
base.start_html()
print("<table>")
print("<tr><td align ='center'>Predmet</td><td align='center'>Bodovi</td><td align='center'>Godina</td><td align='right'>Status</td></tr>")

subjects = db.get_subjects()
enum = ["passed", "enr"]

for subject in subjects:
    status = random.choice(enum)		

    print("""
        <tr>
            <td>""",subject[2],"""</td>
            <td align='center'>""", subject[3],"""</td>
            <td align='center'>""",subject[4],"""</td>
            <td align='center'>""",status,"""</td>
        </tr>
        """)
    db.fill_upisni(subject[0],user_id,status)

print("</table>")

base.finish_html()