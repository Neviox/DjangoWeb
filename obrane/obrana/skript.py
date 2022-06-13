#!C:\Users\Rogulj\AppData\Local\Programs\Python\Python310\python.exe
# import cgi
# from http import cookies
# import os
# import subjects

# params = cgi.FieldStorage()
# cookie = cookies.SimpleCookie()
# def setCookies():
#     isExistedHasBefore = False
#     cookie_string = os.environ.get("HTTP_COOKIE",'')
#     cookie.load(cookie_string)
#     if(cookie.get(params.getvalue("button")) is not None):
#         isExistedHasBefore = True

#     for key,value in subjects.subjects.items():
#         if(params.getvalue("button") == key):
#             cookie[key] = value["name"]
    
#     return isExistedHasBefore

# neverExistedOrIs = setCookies()
# print(cookie)

# def getHTMLBrateu():
#     html = ""

#     for key, value in subjects.subjects.items():
#         html += ''' Name: '''+value["name"]+'''
#         <button name = "button"  value = "'''+key+'''" type="submit">Submit</button><br>


#         '''
#     return html

# def isHasExistedIs(localNeverExistedOrIs):
#     html = ""
#     if (localNeverExistedOrIs is True):
#         html = "kuki postoji!!!!!!!!!!!!!!"
#     return html


# print('''
# <html>
# <head></head>
# <form action = "./skripta.py" method = "post">

# '''+getHTMLBrateu()+'''
# '''+isHasExistedIs(neverExistedOrIs)+'''

# </form>
# </body>
# </html>
# '''
# )



# cookies_string = os.environ.get("HTTP_COOKIE",'')
# cookie.load(cookies_string)
# print(cookie.output())
# if hasExistedIs == True:
#     print("<br>K    U    K    I     P    O    S    T    O    J    I    !!!!!!!!!!!!!!")






import cgi
from http import cookies
import os
import subjects

cookie = cookies.SimpleCookie()
params = cgi.FieldStorage()


def setCookies():
    cookie_string = os.environ.get("HTTP_COOKIE",'')
    cookie.load(cookie_string)
    boolExists = False
    if(cookie.get(params.getvalue("button")) is not None):
        return True
    for key, value in subjects.subjects.items():
        if(params.getvalue("button") == key):
            cookie[key] = value["ects"]
    return False


bExists = setCookies()
print(cookie)


def renderDoesExist(localExists):
    html = ""
    if localExists is True:
        html = "<br>vec postoji"
    return html

def renderHTML():
    html = ""

    for key,value in subjects.subjects.items():
        html += ''' Name: '''+value["name"]+'''<br>
        <button name="button" value='''+key+'''>submit</button><br>

    '''
    return html

print('''

    <html>
    <head></head>
    <body>
    <form action = "./skripta.py" method = "post">
    '''+renderHTML()+'''
    '''+renderDoesExist(bExists)+'''
    </body>
    </html>
    '''
)

cookie_string = os.environ.get("HTTP_COOKIE",'')
cookie.load(cookie_string)
print(cookie.output())




# import os
# import cgi
# from http import cookies


#napravi formu koja ima dva input text fielda, key i value, i kada 
# stisnemo na submit da nas vrati na istu stranicu gdje
# ispise coockie gdje je u jednom spremljen key, a u drugom value

# params = cgi.FieldStorage()

# cookie = cookies.SimpleCookie()
# cookie_string = os.environ.get("HTTP",'')
# cookie.load(cookie_string)

# if params:
#     cookie[params.getvalue("key")] = params.getvalue("value")

# print(cookie)

# print('''
# <html>
# <head></head>
# <body>
# <form action = "./skripta.py" method = "post">
# Key:<input type = "text" name = "key" value =""><br>
# Value:<input type = "text" name = "value" value = ""><br>
# <button name ="button" value="0" type = "submit">submit</button><br>


# </form>
# </body>
# </head>

# ''')
# print(cookie.output())


















































# # napraviti formu sa dva inputa, jedan je ime i prezime studenta, a drugi 
# # radio status da li je redovan ili izvanredan
# # to spremiti u cookie i kada submitamo da nam ispise vrijednosti u cookima

# import os
# import cgi
# from http import cookies


# params = cgi.FieldStorage()
# cookie = cookies.SimpleCookie()

# cookie_string = os.environ.get("HTTP",'')
# cookie.load(cookie_string)


# if params:
#     cookie["name"] = params.getvalue("name")
#     cookie["lastName"] = params.getvalue("lastName")
#     cookie["status"] = params.getvalue("status")

# print(cookie)
 



# print('''
# <html>
# <head></head>
# <body>
# <form action = "./skripta.py" method = "post">
# Ime: <input type = "text" name = "name" value = ""><br>
# Prezime: <input type = "text" name = "lastName" value = ""><br>
# Redovan <input type = "radio" name = "status" value = "redovan"><br>
# Vanredan <input type = "radio" name = "status" value = "vanredan"><br>
# <button name = "button" value = "0" type = "submit">submit</button><br>


# </form>
# </body>
# </html>
# '''
# )

# if params:
#     print(params.getvalue("name"))
#     print(params.getvalue("lastName"))
#     print(params.getvalue("status"))

# if params:
#     print(cookie.get("name").value)
#     print(cookie.get("lastName").value)
#     print(cookie.get("status").value)

# print('''<br><input type = "visible" name = "name" value = "mojValue">''')