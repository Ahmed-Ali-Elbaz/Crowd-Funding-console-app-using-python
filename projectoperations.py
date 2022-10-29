import time
import datetime

def askfornum(message):
    num = input(message)
    
    try:
        num = int(num)
    except:
        return askfornum(message)
    else:
        return str(num)

def askforstring(message):
    string = input(message)
    
    if string.isspace() or not string:
        print("Please insert suitable string!!")
        return askforstring(message)
    
    return string


def askfordetails():
    
    title       = askforstring("Please enter title: ")
    details     = askforstring("Please enter Details: ")
    totaltarget = askfornum("PLease enter Total target(EGP): ")
    startdate   = askfordate("Please enetr Start date(YYYY-MM-DD): ")
    enddate     = askfordate("Please enetr End date(YYYY-MM-DD): ")

    
    return title, details, totaltarget, startdate, enddate, usercode

def askfordate(message):
    
    projdate = input(message)
    
    try:
            datetime.datetime.strptime(projdate, '%Y-%m-%d')
            
    except:
            print("Incorrect data format, should be YYYY-MM-DD")
            askfordate()
        
    else:
        return str(projdate)
        
        
def generate_id():
    id = round(time.time())
    return str(id)



# Create a new Project

def createnewproject():

    print("\n\t\t( Create a new Project )\n")
    projectinfo = list(askfordetails())    
    id = generate_id()
    projectinfo.insert(0, str(id))
    
    # Prepare project information
    projectinfo = ":".join(projectinfo)
    print(projectinfo)
    
    # save project information into a file
    new_project = saveProjectinfo(projectinfo)
    
    if new_project:
        print("a new Project is Created successfully!!")
    else:
        print("Creating a new Project is Faild!!!")
        return createnewproject()   


# Save Project Details in a file
def saveProjectinfo(prodetails):
    try:
        proinfo = open("projectsinfo.txt", "a")
    except:
        print("issue while creating a new Project!!")
        return False 
    else:
        proinfo.write(f"{prodetails}\n")
        return True  





def get_projects_from_file():
    
    try:
        projobj = open("projectsinfo.txt", "r")
    except Exception as e:
        print("error happend wile opennig the file!!!")
        return False
    else:
        projects = projobj.readlines()
        projobj.close()
        return projects   
    


def listallprojects():
    
    # get projects data from projectsinfo.txt
    projects = get_projects_from_file()
    
    if projects == False:
        print("no, available Projects")
    else:
        print(projects)
        



def search_project_by_id(project_id):
    allproject = get_projects_from_file()
    
    for project in allproject:
        myproject = project.strip("\n")
        myproject = myproject.split(":")

        if myproject[0] == project_id:
            project_index = allproject.index(project)

            print(f"Project is found at index {project_index}")
            return True, project_index
    
    else:
        print("Project is not found!!")
        return



def write_project_list_to_file(projectlist):
    
    try:
        projobj = open("projectsinfo.txt", "w")
    except Exception as e:
        print("error happend wile opennig the file!!!")
        return False
    else:
        projobj.writelines(projectlist)
        projobj.close()
        return True    


def delete_project_from_file(project_id):
    
    project_found = search_project_by_id(project_id)
    project_index = project_found[1]
    
    allprojects =  get_projects_from_file()   
    del allprojects[project_index]
    #print(allprojects)

    deleted = write_project_list_to_file(allprojects)
    return deleted


def deleteproject():
    
    listallprojects()
    project_id = askfornum("Please choose id of the book you want to delete: ")
    deleted = delete_project_from_file(project_id)
    
    if deleted:
        print("Project Deleted Successfully")
    