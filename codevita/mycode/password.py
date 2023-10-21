import re

def check_password(password):
    if not password:
        return -1
    if len(password)<8:
        return 0
    if not re.search(r'[A-Z]',password):
        return 0
    if not re.search(r'[a-z]',password):
        return 0
    if not re.search(r'\d' , password):
        return 0
    if '@' not in password:
        return 0 
    if not re.search(r'[^A-Za-z\d@]',password):
        return 0

    return 1
    

    

password=input("ENTER A PASSWORD TO CHECK THE VALIDITY : ")
result =  check_password(password)

if result == -1:
    print('output = -1 (Empty password)')
if result == 0:
    print('output = 0 (Password is invalid)')
if result == 1:
    print('output = 1 (password is valid)')
        