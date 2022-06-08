#!C:\Python310\python.exe
import db
import cgitb

cgitb.enable(display=0,logdir="")

def get_user(user_id):
	try:
		return db.get_user(user_id)
	except:
		return None

def get_user_by_username(username):
	try:
		return db.get_user_by_username(username)
	except:
		return None

def get_user_role(user_id):
	try:
		user_role = db.get_role(user_id)
		return user_role
	except:
		return None

def get_all_users():
	return db.get_users()

def get_student_users():
    try:
        return db.get_student_users()
    except:
            return None
        
def get_admin_users():
    try:
        return db.get_admin_users()
    except:
        return None
    
def delete_user(user_id):
	try:
		db.delete_user(user_id)
	except:
		pass

def update_user(user_id, username, gender, role_id):
	try:
		db.update_user(user_id, username, gender, role_id)
	except:
		print("<h1>ERROR</h1>")