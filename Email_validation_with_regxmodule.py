# codingwithmoez

import re
email_conditions = r"^[a-z][a-z0-9._]*@[a-z0-9.-]+\.[a-z]{2,}$"

user_email = input("Enter the email: ")

if re.search(email_conditions, user_email, re.IGNORECASE):
    print("Correct email")
else:
    print("Wrong Email")