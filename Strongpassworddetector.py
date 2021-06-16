import re
import random
def uppercase_check(password):
    if re.search('[A-Z]', password):
        return True
    return False

def lowercase_check(password):
    if re.search('[a-z]', password):
        return True
    return False

def digit_check(password):
    if re.search('[0-9]', password):
        return True
    return False

def user_input_password_check():
    password = input("Enter password : ")
    if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password):
        print("Strong Password")
    else:
        print("Weak Password")

user_input_password_check()
