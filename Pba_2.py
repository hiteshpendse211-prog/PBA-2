import re

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$!%*?&]).{8,}$'

    if re.match(pattern,password):
        print(password,"-Valid password")
    else:
        print(password,"-Invalid password")

    validate_password-password(input())