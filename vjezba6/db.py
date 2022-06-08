import mysql.connector #!C:\Python310\python.exe -m pip install mysql-connector 
import json
import password_utils
import model

db_conf = {
    "host":"localhost",
    "db_name": "vjezba5",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],  
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def create_user(username, password, email):
    query = "INSERT INTO users (username, email, password) VALUES (%s,%s,%s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password, email)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 

def get_user(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = cursor.fetchone()
    return myresult

def get_users():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    return myresult

def get_user_by_email(email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE email='" + email + "'")
    myresult = cursor.fetchone()
    return myresult

def update_user_password(username, password):
    hashed_password = password_utils.hash_password(password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    UPDATE users SET password=%s WHERE username=%s
    """,
    (hashed_password, username))
    mydb.commit()


def get_role(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id='" + str(id) + "'")
    myresult = cursor.fetchone()
    return myresult[4]

def insert_subjects():
    mydb=get_DB_connection()
    cursor=mydb.cursor()
    subjects = model.get_subjects()
    for i in subjects:
            kod = i
            ime = subjects.get(i, {}).get("name", "n/a")
            bodovi = subjects.get(i, {}).get("ects", "n/a")
            godina = subjects.get(i, {}).get("year", "n/a")
            query = "INSERT INTO subjects (ime,kod,bodovi,godina) VALUES (%s,%s,%s,%s)"
            values = (ime,kod,bodovi,godina)
            try:
                cursor.execute(query, values)
                mydb.commit()
            except:
                return None
            
def get_subjects():
    mydb=get_DB_connection()
    cursor=mydb.cursor()
    cursor.execute("SELECT * FROM subjects")
    myresult = cursor.fetchall()
    return myresult

def fill_upisni(subjects_id,users_id,status):
    mydb=get_DB_connection()
    cursor=mydb.cursor()
    query=("INSERT INTO upisni_list(subjects_id,users_id,status) VALUE (%s,%s,%s)")
    values=(subjects_id,users_id,status)           
    cursor.execute(query,values)
    mydb.commit()