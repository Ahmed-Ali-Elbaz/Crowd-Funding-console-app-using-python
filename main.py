from registration import userregistration
from infohandler import validatelogin

print("\n\t\t=== Welcome to Crowding-Funding Console App ===\n")


def mainmenu():
    choice = input("Please enter (r) to 'register' in our App or (l) to 'login' if u already have an account:  ")
    
    if choice == "r":
        userregistration()
    elif choice == "l":
        validatelogin()
    else:
        print("no correct choice!!")
        mainmenu()
   
mainmenu()
