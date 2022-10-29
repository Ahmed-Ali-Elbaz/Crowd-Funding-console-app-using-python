import re
import time
from infohandler import saveRegistrationinfo


# create  askforname function to get firstname && lastname from user.
def askforname(message):
    name = input(message)
    
    if name.isspace() or not name:
        print("Please insert suitable name!!")
        return askforname(message)
    
    return name

# create  askforphone function to get user phone and validate it is an egyptian number.
def askforphone(message):
    phone = input(message)
    phonePattern = "^01[0125][0-9]{8}$"
    
    
    if re.match(phonePattern,phone):
        return str(phone)
    else:
        
        print("invalid Phone number!!")
        return askforphone(message)
    
# create  askforemail function to get user email in this form @domainname (.com ......).
def askforemail(message):
    email = input(message)
    mailPattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    
    if re.match(mailPattern,email):
        return str(email)
    else:
        print("invalid email Pattern!!")
        return askforemail(message)

# create  askforpassword function to get user password and confirm it.
def askforpassword(message):
    password = input(message)
    confirmpassword = input("Please confirm Password: ")
    
    if confirmpassword == password:
        return str(password)
    else:
        print("Passwords don't match!!")
        askforpassword(message)

# take information from the user (firstname) (lastname) (email) (password) (confirm password) (mobile phone 'Egyptian')    
def askforinformation():
    
    firstname       = askforname("Please enter firstname: ")
    lastname        = askforname("Please enter lastname: ")
    email           = askforemail("Please enter e-mail: ")
    password        = askforpassword("Please enter a Password: ")
    mobilePhone     = askforphone("Please enter Phone number (Egyptian-only!!): ")
    
    return firstname, lastname, email, password, mobilePhone
    
def generate_id():
    id = round(time.time())
    return id










# userregisetration function to get registration information from the user
def userregistration():
    print("\n\t\t== Welcome to (Registration) form ===\n")
    userinfo = list(askforinformation())    
    id = generate_id()
    userinfo.insert(0, str(id))
    
    # Prepare user information
    userinfo = ":".join(userinfo)
    
    # save user information into a file
    new_user = saveRegistrationinfo(userinfo)
    if new_user:
        print("Registration done successfuly!!")
    else:
        print("Registarion Faild!!!!")
        return userregistration()

