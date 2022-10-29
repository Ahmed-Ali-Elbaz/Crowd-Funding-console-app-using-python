
import re
from projectcampaign import projectmenu

def askforemail(message):
    email = input(message)
    mailPattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    
    if re.match(mailPattern,email):
        return str(email)
    else:
        print("invalid email Pattern!!")
        return askforemail(message)


def saveRegistrationinfo(infodetails):
    try:
        reginfo = open("registrationinfo.txt", "a")
    except:
        print("issue while registration process !!")
        return False 
    else:
        reginfo.write(f"{infodetails}\n")
        return True  



def validatelogin():
    
    print("\n\t\t== Welcome back (login) form ===\n")
    email = askforemail("Enter e-mail: ")
    password = input("Enter login Password: ")  
    
    try:
        loginfo = open("registrationinfo.txt", "r")
    except Exception as e :
        print(" error happend while openning the file  ")
    else:
        
        credintials = loginfo.readlines()
        loginfo.close()
        
        for info in credintials:
            myinfo = info.strip("\n")
            myinfo = myinfo.split(":")
            
            if myinfo[3] == str(email) and myinfo[4] == str(password):                
                print("\n\t\tWelcome!!\n")
                
                break

        else:
            print("Wrong e-mail or password!!") 
            validatelogin()
        
        projectmenu()
        
        
