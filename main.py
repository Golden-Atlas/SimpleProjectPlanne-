import time
import json

#Project planning class
class ProjectPlanner:
    def __init__(self):
        self.project={} #initialized dictionary as self.project

    def addProject(self):
        try:
            usert = input('Title of project (type \'12345\' to exit): ') #tempoary, local input variables
            if usert == '12345':
                return None
            else:
                userl = input('What languages are needed for the project?: ')
                userd = input('Write your description of the project: ')
                users = input('Current status of the project (Not Started, In Progress, Abandoned, Completed): ')
                while users.title()!='Not Started' and users.title()!='In Progress' and users.title()!='Abandoned' and users.title()!='Completed':
                    users = input('Not an avaliable option.\nCurrent status of the project (Not Started, In Progress, Abandoned, Completed): ')

                self.project[usert]= {
                    'Languages Needed: ' : userl,
                    'Description: ' : userd,
                    'Status: ' : users.title()
                }
                return
        except:
            print('Error. Shutting down current process')
            time.sleep(2) #waits 2 seconds before proceeding 
            print('\n\n\n\n')
            return

    def deleteProect(self):
        userdelete = input('Title of project would you like to edit (case-sensitive): ')
        if userdelete not in self.project:
            print('Project not found.\n\n\n')
            return
        print('\n')
        for key in self.project[userdelete]:
            print(f'     -{key}{self.project[userdelete][key]}')
        print('-------------------------------------------------------------------\n')

        temp = input(f'Enter "1" to confirm deletion of {userdelete}')
        if temp != '1':
            return
        else:
            del self.project[userdelete]
            return


    def editProject(self):
        usert = input('Title of project would you like to edit (case-sensitive): ')
        if usert not in self.project:
            print('Project not found.\n\n\n')
            return

        print('\n')
        for key in self.project[usert]:
            print(f'     -{key}{self.project[usert][key]}')
        print('-------------------------------------------------------------------\n')


        try:
            userchoice=int(input('1: Edit Languages Needed\n'
                                 '2: Edit Description\n'
                                 '3: Edit Status\n'
                                 '4: Exit Menu\n'
                                 'Choice: '))
            if userchoice==1:
                userl = input('What languages are needed for the project?: ')
                self.project[usert]['Languages Needed: '] = userl
                return

            elif userchoice==2:
                userd = input('Write your description of the project: ')
                self.project[usert]['Description: '] = userd
                return

            elif userchoice==3:
                users = input('Current status of the project (Not Started, In Progress, Abandoned, Completed): ')
                while users.title()!='Not Started' and users.title()!='In Progress' and users.title()!='Abandoned' and users.title()!='Completed':
                    users = input('Not an avaliable option.\nCurrent status of the project (Not Started, In Progress, Abandoned, Completed): ')
                self.project[usert]['Status: '] = users.title()
                return

            elif userchoice==4:
                print("Exiting...\n\n")
                return


        except:
            print('Error. Shutting down current process')
            time.sleep(2)
            print('\n\n\n\n')
            return




    def exportData(self):
        with open('projectDict.json', 'w') as file:
            json.dump(self.project, file)
            file.close()
            return

    def importData(self):
        with open('projectDict.json', 'r') as file:
            self.project = json.load(file)
            file.close()
            return



    def print(self):
        for key, value in self.project.items():
            print(key)
            for i, k in value.items():
                print(f'     -{i}{k}')
            print('-------------------------------------------------------------------')
            return



plan = ProjectPlanner()
while True:
    print('-------------------------------------------------------------------')
    print('Choose from the following options:\n'
          '1: Add a project\n'
          '2: Delete a project\n'
          '3: Edit a project\n'
          '4: Export the current project list\n'
          '5: Import the currently externally saved project list\n'
          '6: Print the current project list\n'
          '7: Exit the menu (remember to save)')
    try:
        userchoice = int(input('Choice: '))

        if userchoice==1:
            plan.addProject()
        elif userchoice==2:
            plan.deleteProect()
        elif userchoice==3:
            plan.editProject()
        elif userchoice==4:
            plan.exportData()
        elif userchoice==5:
            plan.importData()
        elif userchoice==6:
            plan.print()
        elif userchoice==7:
            print('Have a good day!\n\n\n')
            quit()
        else:
            print('Invalid, please try again\n\n\n\n\n\n')

    except:
        print('Error, try again.')
        tempuser = input('Press "Enter" to continue"')

