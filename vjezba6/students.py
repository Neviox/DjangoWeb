#!C:\Python310\python.exe
import base
import cgi
import session
import users_controller
import cgitb

cgitb.enable(display=0,logdir="")

params = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print ("Location: login.py")
else:
	user_id=data.get("user_id",None)
	user_role = users_controller.get_user_role(user_id)
	if user_role != "admin":
		print()
		base.start_html()
		print("Nemate pravo pristupa")
		print('<br></br>',user_role)
		print('<br></br><a href="index.py">Home</a>')
		base.finish_html()
	else:		
		print ()
		base.start_html()
		print ("<h1>USERS:</h1>")
		users = users_controller.get_all_users()
		print ("<table border=1>")
		for user in users:
			print ("<tr>")
			print ("<td>" + user[1] + "</td>")
			print('<td><a href="upisni_list.py?user_id='+ str(user[0]) +'"">Upisni list</a></td>')
			print ("</tr>")
		print ('<tr><td><a href="register.py">add user</a></td></tr>')
		print ("</table>")
		base.finish_html()

