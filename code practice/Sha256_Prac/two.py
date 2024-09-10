import hashlib
import os

def generate_salt():
    random_salt= os.urandom(16)
    print(f"Random generated Salt= {random_salt}")
    return random_salt

def sha256_hash(password, salt):
    salted_password= password.encode('utf-8')+ salt 
    print(f"password= {password}\n salted password= {salted_password}")
    return salted_password, salt    

def encrypt(password):
    salt= generate_salt()
    hased_password= sha256_hash(password, salt)
    return hased_password, salt

password= "My_Password"
salted_password, salt= encrypt(password)

print(f"Hashed Password: {salted_password}")
print(f"Salt: {salt}")