def email_validator(email):
    str = ""
    if "@" not in email:
        str += "Email must contain '@' symbol. "
    
    if "." not in email:
        str += "Email must contain '.' symbol. "

    return str

email = input("Enter your email address: ")
validation_result = email_validator(email)
print(validation_result if validation_result else "Email is valid.")