# Import date for later use in assigning tasks.
import datetime

# ====== LOGIN SECTION ======
# Open user data from user.txt and store in list.
user_data = []
with open("user.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        user_data.append(line)

# Ask user for their username and password and store login details.
print("──── LOGIN: ────────────────────────")
username = input("Enter your username: ")
password = input("Enter your password: ")
login_details = f"{username}, {password}"

# If details are incorrect or non-existent, prompt user to try again.
while login_details not in user_data:
    print("Your details are incorrect or do not exist. Please try again!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_details = f"{username}, {password}"


while True:

 
    # ===== FUNCTIONS =====
    def reg_user():
        again = "y"

        while again == "y":
            
            print("\nREGISTRATION:")
            print("──────────────────────────────────────────────────")

            # Request new username for registration.  If username already exists in user.txt, ask user to choose a different one. 
            new_user = input("Please register a username: ")
            with open("user.txt", "r") as f:
                data = f.read()
                while new_user in data:
                    new_user = input("Username Taken! Please register a different username: ")


            # Request new password for registration and ask user to confirm new password.
            # While password inputs dont match, re-prompt password from user.
            new_pass = input("Create a password: ")
            pass_confirm = input("Confirm password: ")

            while new_pass != pass_confirm:
                print("Passwords dont match, try again!")
                new_pass = input("Create a password: ")
                pass_confirm = input("Confirm password: ")
            
            # Open user.txt file and write/append new user details to file on new line.
            with open("user.txt", "a+") as f:
                f.write(f"\n{new_user}, {new_pass}")

            again = input("Register another user? y/n: ")
    
    def add_task():
        # Set new_task variable to yes as baseline.
            new_task = "y"
            
            print("\n ADD NEW TASK:")
            print("──────────────────────────────────────────────────")
            # While new_task equals 'yes': ask user to input details of the task, description, user assignment and assignment date.
            # Add each detail to task_details variable; ensuring to separate each piece of information with '/' for later list splitting.
            while new_task == "y":
                
                task_details = input("Task Name: ")
                task_details = f"{task_details}/{input('Task Description: ')}"
                task_details = f"{task_details}/{input('Assign to: ')}"
                task_details = f"{task_details}/{(datetime.date.today()).strftime('%d.%m.%Y')}"
                task_details = f"{task_details}/{input('Due Date [dd.mm.yyyy]: ')}"
                task_details = f"{task_details}/no"
                
                # Write/append task_details to tasks.txt file to store on a new line.
                with open("tasks.txt", "a+") as f:
                        f.write(f"\n{task_details}")
                
                # Ask user if they wish to add another task.
                new_task = input("\nAdd another task? y/n: ")
    
    def view_all():
        
        print("\nALL TASKS:")
            
        # Open tasks.txt file and split the contents of each line into lists via '/'.   
        with open("tasks.txt", "r+") as f:
            for line in f:

                # Ensure to remove '\n' prior to list creation.
                line = line.replace("\n","")            
                task_details = line.split("/")
                
                # Print task details in a clear format, in accordance with their index position in task_details list.
                print("\n─────────────────────────────────────────────────────────────────────────────────────────────────") 
                print(f"Task:                 {task_details[0]}")
                print("─────────────────────────────────────────────────────────────────────────────────────────────────") 
                print(f"Task Description:     {task_details[1]}")
                print(f"Assigned to:          {task_details[2]} on {task_details[3]}")
                print(f"Due Date:             {task_details[4]}")
                print(f"Task Complete?:       {task_details[5]}")
                print("─────────────────────────────────────────────────────────────────────────────────────────────────\n") 
            
    def view_mine():

            # Display user tasks label 
            print(f"\nTasks Assigned to {username}:")
            
            # Open tasks.txt and save each line of information as a nested list within a 'data' list.
            with open("tasks.txt", "r") as f:
                data = []
                for index, line in enumerate(f):
                    line = line.replace("\n", "")
                    line = line.split("/")
                    data.append(line)              
                    
                    
                    # Print Each task and its information to user in a user friendly manner.
                    print("\n─────────────────────────────────────────────────────────────────────────────────────────────────") 
                    print(f"Task #{index+1}:      {data[index][0]}")
                    print("─────────────────────────────────────────────────────────────────────────────────────────────────") 
                    print(f"Task Description:     {data[index][1]}")
                    print(f"Assigned to:          {data[index][2]} on {data[index][3]}")
                    print(f"Due Date:             {data[index][4]}")
                    print(f"Task Complete?:       {data[index][5]}")
                    print("─────────────────────────────────────────────────────────────────────────────────────────────────\n") 
                    
                

            # Create while True loop to enable multiple edits in one session.
            while True:

                edit = input("Edit a task? y/n: ") # FIX REPETITION LATER # TODO
                if edit == "n":
                    break

                # Ask user which task they would like to edit.
                # If the task does not exist, prompt user to try again.
                task_choice = int(input("Which task would you like to edit?: ")) -1
                
                while task_choice < 0 or task_choice > len(data) -1:
                    print("This task does not exist. Please choose another task to edit.")
                    task_choice = int(input("Which task would you like to edit?: ")) -1

                while data[task_choice][-1] == "yes":
                    another = input("Completed tasks can't be edited. Would you like to edit a different task? y/n: ")
                    if another == "y":
                        task_choice = int(input("Which task would you like to edit?: ")) -1
                        continue
                    else:
                        break
                
                # Print option menu to user and ask user to choose an action.
                # If input is invalid, prompt user to try again.
                print("\nACTIONS:  Please select one of the following options:")
                print("──────────────────────────────────────────────────")
                print("► 1 - Mark task complete \n► 2 - Edit user assigned to task\n► 3 - Edit due date")
                print("──────────────────────────────────────────────────")
                action = int(input("which action would you like to perform?: "))
            
                while action < 1 or action > 3:
                    print("This is not a valid option. Please try again.")
                    action = int(input("which action would you like to perform?: "))



                # If user selects action 1, the nested element corresponding with task completion (data[task_choice][-1]) is converted to 'yes'.
                if action == 1: 
                    data[task_choice][-1] = "yes"
                    
                # If user selects action 2, the nested element corresponding with assigned user (data[task_choice][2]) is changed to new user input.
                elif action == 2:
                    data[task_choice][2] = input("Enter the username of the person the task will be reassigned to: ")
                    
                # If user selects action 3, the nested element corresponding with due date (data[task_choice][4]) is changed to new user input.
                else: # ==3
                    data[task_choice][4] = input("Enter new due date [dd.mm.yyyy]: ")
                    


                # Ask user if they would like to make another adjustment.
                # If 'y' continue to top of loop.  If 'no', break.
                again = input("Would you like to edit another task? y/n: ")
                if again == "y":
                    continue
                else:
                    break


            # Open tasks.txt
            # For each element in data, rejoin data as str separated by '/' and ensure to append '\n' for file readability.  Write to tasks file.
            with open("tasks.txt", "w") as f:
                for element in data:
                    element = "/".join(element) # should join back to str
                    element = element +"\n"
                    f.write(element)

    def generate_report(): 
    
        # ===== TASK OVERVIEW SECTION =====

        # Open task.txt file.
        with open("tasks.txt", "r") as tasks_f:
            
            # Save each line of information as a nested list within a 'data' list.
            data = []
            for line in tasks_f:
                line = line.replace("\n", "")
                line = line.split("/")
                data.append(line)              
                    
        # Create baseline count variables and todays date storage variable for later use.      
        total_tasks = 0
        completed_tasks = 0
        overdue = 0
        incomplete_overdue= 0
        today = datetime.date.today()
        overdue_tasks =[]

        # For each piece of data in data:
        for index, line in enumerate(data):
            total_tasks += 1

            # Convert due date to date format for date comparison.
            due_date = datetime.datetime.strptime(data[index][-2], '%d.%m.%Y').date()
            
            # If completion index [-1] is 'yes', completed tasks +1.
            if data[index][-1] =="yes":
                completed_tasks += 1
            
            # If todays date is later (>) than the due date, +1 to the overdue variable and append the task to overdue_tasks list for later user analysis.
            if today > due_date:
                overdue += 1
                overdue_tasks.append(line)


        # Calculate percentage of tasks completed and the percentage of incomplete tasks.
        complete_percent = round((completed_tasks/total_tasks*100), 2)
        incomplete_tasks = total_tasks - completed_tasks
        incomplete_percent = round((incomplete_tasks/total_tasks*100), 2)


        # For all overdue tasks saved to overdue_tasks, if the completion index [-1] is 'no', 'incomplete_overdue' +1.
        # Calculate the percentage of tasks which are both incomplete and overdue.
        for index, item in enumerate(overdue_tasks):
            if overdue_tasks[index][-1] == "no":
                incomplete_overdue += 1
        incomplete_overdue_percent = round((incomplete_overdue/total_tasks*100), 2)


        # Add collected data to task_overview list and write it to task_overview.txt file.
        task_overview = f"{total_tasks}/{completed_tasks}/{complete_percent}/{incomplete_tasks}/{incomplete_percent}/{incomplete_overdue}/{incomplete_overdue_percent}"
        with open("task_overview.txt", "w") as f:
                f.write(task_overview)

        print("Report generated.")



        # ===== USER OVERVIEW SECTION =====

        # Open user.txt file.
        with open("user.txt", "r") as user_f:

            # Create baseline count variables and lists for later analysis.
            total_users = 0
            user_data = []
            task_assignees = []
            completed_tasks = []

            # For each line in user.txt, save usernames (line[0]) to the user_data list.
            for line in user_f:
                total_users += 1
            
                line = line.replace("\n", "")
                line = line.split(", ")
                user_data.append(line[0])         


        # For each task saved in 'data' add the user assigned to that task (data[index][2]) to task_assignees list for later analysis.
        for index, line in enumerate(data):
            task_assignees.append(data[index][2])

            
            # For each task saved in 'data', if the completion index (data[index][-1]) is 'yes': 
            # add the user assigned to that task (data[index][2]) to completed_tasks list for later analysis.
            if data[index][-1] =="yes":
                completed_tasks.append(data[index][2])


        # Create empty user_overview list to store analysis results in.
        user_overview = []

        # For each user in data:
        for user in user_data: 
            
            user_overdue = 0

            # For each time user appears in overdue_tasks, user_overdue +1.
            for index, item in enumerate(overdue_tasks):
                if overdue_tasks[index][2] == user:
                    user_overdue += 1

            # Count how many times user appears in task_assignees and completed_tasks:
            # Assign to tasks_assigned_to_user and completed_by_user respectively.
            tasks_assigned_to_user = task_assignees.count(user)
            completed_by_user = completed_tasks.count(user)

            # Calculate % equivalents of data collected so far and store for later statistics display.
            percent_of_all = round((tasks_assigned_to_user/total_tasks*100), 2)
            percent_of_users_complete = round((completed_by_user/tasks_assigned_to_user*100), 2)
            percent_of_users_incomplete = round(((tasks_assigned_to_user - completed_by_user)/tasks_assigned_to_user*100), 2)
            percent_of_users_overdue = round((user_overdue/tasks_assigned_to_user*100), 2)

            # Store collected data for each user in user_store list and nest it within the general user_overview list.
            user_store = f"{user}/{tasks_assigned_to_user}/{percent_of_all}/{completed_by_user}/{percent_of_users_complete}/{tasks_assigned_to_user - completed_by_user}/{percent_of_users_incomplete}/{user_overdue}/{percent_of_users_overdue}"
            user_overview.append(user_store)
            with open("user_overview.txt", "w") as f:

                # For each data piece in user_overview, write the data to user_overview.txt ensuring to add '\n'
                for item in user_overview:
                    f.write(f"{item}\n")

    def view_stats():
        
            # ===== GENERAL STATISTICS =====

            # Create 'task' and 'user' count variables with baseline values of 0.
            task_count = 0
            user_count = 0

            # Open tasks.txt file and increase task_count by 1 for each line of file.
            with open("tasks.txt", "r+") as f:
                    for line in f:
                        task_count += 1
            
            # Open user.txt file and increase user_count by 1 for each line of file.
            with open("user.txt", "r+") as f:
                    for line in f:
                        user_count += 1

            # Print task and user statistics.
            print( "\n───────────────────────────────────────────────")
            print( "   GENERAL STATISTICS")
            print( "───────────────────────────────────────────────")
            print(f"  Total Number of Tasks: {task_count}")
            print(f"  Total Number of Users: {user_count}")



            # ===== TASK OVERVIEW SECTION =====

            # Open task_overview.txt and save data to list.
            with open("task_overview.txt", "r") as f:
                task_overview = []
                for line in f:
                    line = line.replace("\n", "")
                    task_overview = line.split("/")
                            
                        
            # Display the data in a user friendly manner using the corresponding list indexes.
            print(f"\n──────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(f"TASK OVERVIEW")
            print(f"──────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(f"Total No. of Tasks:              {task_overview[0]}")
            print(f"Tasks Completed:                 {task_overview[1]}      ({task_overview[2]}% of all tasks)"  )
            print(f"Incomplete Tasks:                {task_overview[3]}      ({task_overview[4]}% of all tasks)")
            print(f"Overdue Tasks:                   {task_overview[5]}      ({task_overview[6]}% of all tasks)")
            print(f"──────────────────────────────────────────────────────────────────────────────────────────────────────\n")



            # ===== USER OVERVIEW SECTION =====

            # Open user_overview.txt.
            with open("user_overview.txt", "r") as f:
                
                # For each line in the file, save its data to a list.
                print("\n[USER OVERVIEWS]")
                for line in f:
                    line = line.replace("\n", "")
                    user_overview = line.split("/")
                            
                    
                    # Display the data in a user friendly manner using the corresponding list indexes.
                    print(f"\n──────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(f"{user_overview[0]}\n──────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(f"• Tasks assigned to {user_overview[0]}:   {user_overview[1]}             ({user_overview[2]}% of all tasks)")
                    print(f"• Tasks completed:           {user_overview[3]}             ({user_overview[4]}% of the tasks assigned to {user_overview[0]}) ")
                    print(f"• Incomplete tasks:          {user_overview[5]}             ({user_overview[6]}% of the tasks assigned to {user_overview[0]})      ")
                    print(f"• Tasks Overdue:             {user_overview[7]}             ({user_overview[8]}% of all tasks assigned to {user_overview[0]})")
                    print(f"──────────────────────────────────────────────────────────────────────────────────────────────────────\n")
            

    # =========== SELECTION MENU: ==============
    # If user is admin, print menu containing: Register, Add Task, View All, View My Tasks, View Stats, Exit.
    if login_details == "admin, adm1n":
        print("\nMENU:  Please select one of the following options:")
        print("──────────────────────────────────────────────────")
        print("► r  -  Register \n► a  -  Add Task \n► va -  View All Tasks \n► vm -  View My Tasks \n► gr -  Generate Reports \n► s  -  View Stats \n► e  -  Exit")
        print("──────────────────────────────────────────────────")
        # Get users selection input.
        menu_selection = input("Selection: ").lower()

    # If user is not admin, print menu containing: Add Task, View All, View My Tasks, Exit.
    else:
        print("\nMENU:  Please select one of the following options:")
        print("──────────────────────────────────────────────────")
        print("► a  -  Add Task \n► va -  View All Tasks \n► vm -  View My Tasks \n► e  -  Exit")
        print("──────────────────────────────────────────────────")

        # Get users selection input.
        menu_selection = input("Selection: ").lower()



    # =========== REGISTRATION MENU: ==============
    if menu_selection == "r":
        reg_user()
        menureturn = input("\nReturn to main menu? y/n: ")
        if menureturn == "y":
            continue

        
    # =========== ADD TASK SELECTION ============
    elif menu_selection == "a":
        add_task()       
        menureturn = input("\nReturn to main menu? y/n:  ")
        if menureturn == "y":
            continue
        else:
            print('\nGoodbye, Thanks for checking in!')
            exit()


    # ============ VIEW ALL =================
    elif menu_selection == "va":
        view_all()
        menureturn = input("\nReturn to main menu? y/n:  ")
        if menureturn == "y":
            continue
        else:
            print('\nGoodbye, Thanks for checking in!')
            exit()


    # ============ VIEW MY FILES =================
    elif menu_selection == "vm":
        view_mine()
        menureturn = input("\nReturn to main menu? y/n:  ")
        if menureturn == "y":
            continue
        else:
            print('\nGoodbye, Thanks for checking in!')
            exit()


    # ============ GENERATE REPORTS =================
    elif menu_selection == "gr":
        generate_report()

        view = input("View reports in statistics? y/n: ")
        if view == "y":
            view_stats()
        else:
            continue

        menureturn = input("\nReturn to main menu? y/n:  ")
        if menureturn == "y":
            continue
        else:
            print('\nGoodbye, Thanks for checking in!')
            exit()


    # ============ VIEW STATS =================
    elif menu_selection == "s":
        view_stats()
        menureturn = input("\nReturn to main menu? y/n:  ")
        if menureturn == "y":
            continue
        else:
            print('\nGoodbye, Thanks for checking in!')
            exit()       


    # ======= EXIT ========
    elif menu_selection == "e":
        print('\nGoodbye, Thanks for checking in!')
        exit()


    else:
        print("\nWoops! Something went wrong. Please Try again.")    