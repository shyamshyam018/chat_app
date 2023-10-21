import re

def check_password_validity(password):
    if not password:
        return -1  
    if len(password) < 8:
        return 0  

    if not re.search(r'[A-Z]', password):
        return 0 
    if not re.search(r'[a-z]', password):
        return 0  
    if not re.search(r'\d', password):
        return 0  
    if '@' not in password:
        return 0 

    if re.search(r'[^A-Za-z\d@]', password):
        return 0 

    return 1 


user_password = input("Enter a password to test its validity: ")
result = check_password_validity(user_password)

if result == -1:
    print("Output: -1 (Empty password)")
elif result == 0:
    print("Output: 0 (Invalid password)")
else:
    print("Output: 1 (Valid password)")
