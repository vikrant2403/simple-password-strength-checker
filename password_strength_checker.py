#simple password strength checker#
import re
user = input("enter username: ")
password = input("enter password: ")
len1 = len(password)
if len1 < 10:
    print("the length is less than 10 characters")
elif not re.search("[a-z]",password):
    print ("there should be a lowercase letter")
elif not re.search("[A-Z]",password):
    print("the password should be uppercase letter")
elif not re.search("[0-9]",password):
    print("there should be a number")
else:
    print("strong password")

