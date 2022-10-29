from projectoperations import createnewproject,listallprojects, deleteproject

def projectmenu():
    choice = input("Please enter:\n (n) to 'create new Project'\n (l) to 'list all Projects'\n (e) to 'edit a Project' \n (d) to 'delete a Project'\n")
    
    if choice == "n":
        createnewproject()
        
    elif choice == "l":
        listallprojects()
        
    elif choice == "e":
        print("Edit a project")
        
    elif choice == "d":
        deleteproject()   
            
    else:
        print("No correct choice!!")
        projectmenu()
        


