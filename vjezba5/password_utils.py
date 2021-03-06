#!C:\Python310\python.exe
import os
import hashlib


def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    hash = salt + key 

    return hash

def verify_password (password, hash):
 
    salt = hash[:32]
    key = hash[32:]

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'), 
        salt, 
        100000)
    return new_key==key 
