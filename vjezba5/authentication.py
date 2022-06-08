#!C:\Python310\python.exe
import db 
import password_utils

def register(username, password, email):
    user_id = db.create_user(username, password, email)
    if user_id:
        return True
    else:
        return False
        
def authenticate(username, password):
    user = db.get_user(username)
    if (user and password_utils.verify_password(password, user[3])):
        return True, user[0]
    else:
        return False, None
        
def change_password(username, new_password):
    db.update_user_password(username, new_password)
