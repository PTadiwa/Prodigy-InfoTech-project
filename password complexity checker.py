
import re

#Password must be at least 8 characters long
password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
    pass
elif not re.search("[A-Z]", password):
    print ("Password must contain at least one uppercase letter.")


elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")

elif not re.search("[0-9]", password):
    print("Password must contain at least one digit.")



else:
    print("Password is strong enough.")