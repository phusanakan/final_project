from database import Database, Login, Project, AdvisorPendingRequest, MemberPendingRequest, Person, Student, Faculty, Admin, SeniorProject, Evaluation
import datetime


def initializing():
    db = Database()
    persons_table = db.add_table('persons', 'persons.csv', Person)
    login_table = db.add_table('login', 'login.csv', Login)
    project_table = db.add_table('project', 'project.csv',Project)
    advisor_pending_request_table = db.add_table('advisor_pending', 'advisor_pending_request.csv', AdvisorPendingRequest)
    member_pending_requese_table = db.add_table('member_pending','member_pending_request.csv', MemberPendingRequest)
    return db


def login(db):
    login_table = db.tables.get('login')  # get table class from db by table name

    if login_table:
        while True:
            username = input('Enter username: ')
            password = input('Enter password: ')
            for person in login_table.rows:  # person => Login()
                if person.username == username and person.password == password:
                    print(".\n.\n.\nLogged in")
                    return person

                print("Invalid username or password. please try again")

    else:
        print("Login table not found.")
        return None


def search_person_by_id(db, person_id, person_type):
    person_table = db.tables.get("persons")
    for person in person_table.rows:
        if person.ID == person_id and person.type == person_type:
            return person
    return None


def search_project_by_id(db, project_id):
    project_table = db.tables.get("project")
    for project in project_table.rows:
        if project.projectID == project_id:
            return project
    return None


def get_all_project_id_of_lead(db, lead_id):
    search_project_id_list = []
    project_table = db.tables.get("project")
    for project in project_table.rows:
        if project.lead == lead_id:
            search_project_id_list.append(project.projectID)
    return search_project_id_list


def get_project_by_project_id(db, project_id):
    project_table = db.tables.get('project')
    for project in project_table.rows:
        if project.projectID == project_id:
            return project
    return None


def print_all_person_by_person_list(db, person_list, person_type):
    person_table = db.tables.get("persons")
    if person_table:
        if person_type != "":
            print(f"All {person_type} detail:")
        for person in person_table.rows:
            if person.ID in person_list:
                print(f"\t- ID: {person.ID}, Firstname: {person.first}, Lastname: {person.last}, Type: {person.type}")
    else:
        print("Person table not found")


def is_project_pending_member(db, project_id):
    member_pending_requese_table = db.tables.get("member_pending")
    if member_pending_requese_table:
        is_pending = False
        for pending in member_pending_requese_table.rows:
            if pending.projectID == project_id and pending.response == "pending":
                is_pending = True
                break
        return is_pending
    else:
        print("member pending request not found")
        return True


def update_login_role(db, update_id, role_name):
    login_table = db.tables.get('login')
    persons_table = db.tables.get('persons')
    if login_table:
        login_table.update(["ID"], [update_id], ["role"], [role_name])
    else:
        print("Login table not found")
        return
    if persons_table:
        persons_table.update(["ID"], [update_id], ["type"], [role_name])
    else:
        print("Persons table not found")
        return


def update_decline_member_by_project_list(db, project_id_list, person_id):
    member_pending_requese_table = db.tables.get("member_pending")
    if member_pending_requese_table:
        if len(project_id_list) > 0:
            for project_id in project_id_list:
                member_pending_requese_table.update(["projectID", "to_be_member"],
                                                    [project_id, person_id],
                                                    ["response", "response_date"],
                                                    ["decline", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                                                    )
    else:
        print("member pending requese table not found")
        return


def update_new_member_to_project(db, project_id, member_id):
    project_table = db.tables.get('project')

    if project_table:
        found_project = get_project_by_project_id(db, project_id)
        if found_project:
            if found_project.member1 != "" and found_project.member2 != "":
                print(f"Member full Can't add new member to Project ID {project_id}")
            elif found_project.member1 == "":
                project_table.update(["projectID"], [project_id], ["member1"], [member_id])
            elif found_project.member2 == "":
                project_table.update(["projectID"], [project_id], ["member2"], [member_id])
    else:
        print("Project table not found")
        return


def update_decline_advisor_by_project_list(db, project_id_list, person_id):
    advisor_pending_request_table = db.tables.get("advisor_pending")
    if advisor_pending_request_table:
        if len(project_id_list) > 0:
            for project_id in project_id_list:
                advisor_pending_request_table.update(["projectID", "to_be_advisor"],
                                                     [project_id, person_id],
                                                     ["response", "response_date"],
                                                     ["decline", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                                                     )
    else:
        print("advisor pending request table not found")
        return


def update_new_advisor_to_project(db, project_id, advisor_id):
    project_table = db.tables.get('project')

    if project_table:
        found_project = get_project_by_project_id(db, project_id)
        if found_project:
            if found_project.advisor != "":
                print(f"Already has advisor Can't add new advisor to Project ID {project_id}")
            else:
                project_table.update(["projectID"], [project_id], ["advisor", "status"],
                                     [advisor_id, "ready to solicit an advisor"])
    else:
        print("Project table not found")
        return


def update_project_status(db, project_id, project_status):
    project_table = db.tables.get("project")
    if project_table:
        project_table.update(["projectID"], [project_id], ["status"], [project_status])
    else:
        print("Project table not found")
        return


# Admin type function
# DONE
def see_all_project_information(db):
    project_table = db.tables.get("project")
    if project_table:
        if len(project_table.rows) == 0:
            print("No project available...!!")
        for project in project_table.rows:
            print(f"• Project ID: {project.projectID}, Project {project.title}, status = ({project.status})")
            print_all_person_by_person_list(db, [project.lead, project.member1, project.member2], "")
    else:
        print("Project table not found")
        return


# DONE
def see_all_student_no_project(db):
    person_table = db.tables.get("persons")
    if person_table:
        print(f"All student information that didn't join any project:")
        for person in person_table.rows:
            if person.type == "student":
                print(f"\t- ID: {person.ID}, Firstname: {person.first}, Lastname: {person.last}, Type: {person.type}")
    else:
        print("Person table not found")


# DONE
def see_all_faculty_no_project(db):
    person_table = db.tables.get("persons")
    if person_table:
        print(f"All faculty information that didn't advise any project:")
        for person in person_table.rows:
            if person.type == "faculty":
                print(f"\t- ID: {person.ID}, Firstname: {person.first}, Lastname: {person.last}, Type: {person.type}")
    else:
        print("Person table not found")


# DONE
def see_all_member_pending_request(db):
    member_pending_request_table = db.tables.get("member_pending")
    if member_pending_request_table:
        if len(member_pending_request_table.rows) == 0:
            print("No member pending request...!!")
            return
        print("List of all member pending:")
        for pending in member_pending_request_table.rows:
            print(
                f"\t- ProjectID: {pending.projectID}, member pending ID: {pending.to_be_member}, response: {pending.response} ({pending.response_date})")
    else:
        print("member pending request table not found")
        return


# DONE
def see_all_advisor_pending_request(db):
    advisor_pending_request_table = db.tables.get("advisor_pending")
    if advisor_pending_request_table:
        if len(advisor_pending_request_table.rows) == 0:
            print("No advisor pending request...!!")
            return
        print("List of all advisor pending:")
        for pending in advisor_pending_request_table.rows:
            print(
                f"\t- ProjectID: {pending.projectID}, advisor pending ID: {pending.to_be_advisor}, response: {pending.response} ({pending.response_date})")
    else:
        print("advisor pending request table not found")
        return


def create_project_by_student(db, person_login):
    title = input('Enter title: ')
    person_id = person_login.ID
    project_id = -1
    project_table = db.tables.get('project')

    if project_table:
        if len(project_table.rows) == 0:
            project_id = 1
        else:
            project_id = int(project_table.rows[-1].projectID) + 1
    else:
        print("Project table not found")
        return

    insert_dict = {
        "projectID": project_id,
        "title": title,
        "lead": person_id,
        "member1": "",
        "member2": "",
        "advisor": "",
        "status": "pending member"
    }
    # insert
    project_table.insert(insert_dict)
    update_login_role(db, person_id, "lead")
    print(f"Created new project name {title}")


# DONE
def see_all_pending_request_for_member(db, person_login):
    member_pending_requese_table = db.tables.get("member_pending")
    if member_pending_requese_table:
        is_no_request = True
        print("List of all project request you to join their team...")
        for pending in member_pending_requese_table.rows:
            if pending.to_be_member == person_login.ID and pending.response == "pending":
                project = search_project_by_id(db, pending.projectID)
                print(f"\t- ProjectID: {project.projectID}, Project {project.title}, status = ({project.status})")
                is_no_request = False
        if is_no_request:
            print("No any member request send to you.....!!!")
    else:
        print("member pending requese table not found")
        return


def accept_member_request(db, person_login):
    member_pending_requese_table = db.tables.get("member_pending")
    if member_pending_requese_table:
        project_id_list = []
        print("List of all project request you to join their team...")
        for pending in member_pending_requese_table.rows:
            if pending.to_be_member == person_login.ID and pending.response == "pending":
                project = search_project_by_id(db, pending.projectID)
                print(f"\t- ProjectID: {project.projectID}: Project {project.title}, status = ({project.status})")
                project_id_list.append(project.projectID)

        if len(project_id_list) == 0:
            print("No any member request send to you.....!!!")
            return

        while len(project_id_list) > 0:
            print()
            print(f"{len(project_id_list)} invitation remain...")
            seleced_project_id = input(
                "Choose project ID you want to accept or deny **can accept only one project** (Enter 0 to exit): ")
            if seleced_project_id == "0":
                break
            elif seleced_project_id in project_id_list:
                while True:
                    accept_flag = input("accept invitation of Project ID {seleced_project_id} (Y/n): ")
                    if accept_flag != "Y" and accept_flag != "n":
                        print("***Input invalid Please select only Y or n only***")
                    else:
                        if accept_flag == "Y":
                            member_pending_requese_table.update(["projectID", "to_be_member"],
                                                                [seleced_project_id, person_login.ID],
                                                                ["response", "response_date"],
                                                                ["accept",
                                                                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                                                                )
                            update_login_role(db, person_login.ID, "member")
                            update_new_member_to_project(db, seleced_project_id, person_login.ID)
                            project_id_list.remove(seleced_project_id)

                            update_decline_member_by_project_list(db, project_id_list, person_login.ID)
                            project_id_list.clear()

                            print(f"accepted invitation of Project ID: {seleced_project_id}")
                            print("-----And decline invitation on other Project-----")
                        else:
                            member_pending_requese_table.update(["projectID", "to_be_member"],
                                                                [seleced_project_id, person_login.ID],
                                                                ["response", "response_date"],
                                                                ["decline",
                                                                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                                                                )
                            project_id_list.remove(seleced_project_id)
                        break
            else:
                print("***Project ID invalid please try again***")
    else:
        print("member pending requese table not found")
        return


def see_project_status(db, person_login):
    project_table = db.tables.get("project")
    if project_table:
        for project in project_table.rows:
            if project.lead == person_login.ID or project.member1 == person_login.ID or project.member2 == person_login.ID:
                print(f"- Project {project.title}; status = ({project.status})")

    else:
        print("Project table not found")
        return


def see_responded_to_request_member(db, person_login):
    project_table = db.tables.get("project")
    member_pending_requese_table = db.tables.get("member_pending")

    if project_table:
        for project in project_table.rows:
            if project.lead == person_login.ID or project.member1 == person_login.ID or project.member2 == person_login.ID:
                print(f"Project {project.title} (ID: {project.projectID})")
                is_all_pending = True
                for member_pending in member_pending_requese_table.rows:
                    if member_pending.projectID == project.projectID and member_pending.response != "pending":
                        is_all_pending = False
                        print(f"\t- student ID: {member_pending.to_be_member} => {member_pending.response}")
                if is_all_pending:
                    print("\t- No response from any student")
    else:
        print("Project table not found")
        return


def see_and_modify_project(db, person_login):
    project_table = db.tables.get("project")
    if project_table:
        project_id_list = []
        print("List of all project of your team")
        for project in project_table.rows:
            if project.lead == person_login.ID or project.member1 == person_login.ID or project.member2 == person_login.ID:
                print(f"\t- ProjectID: {project.projectID}: Project {project.title}, status = ({project.status})")
                project_id_list.append(project.projectID)

        if len(project_id_list) == 0:
            print("No project available.....!!!")
            return

        while True:
            print()
            seleced_project_id = input(
                "Choose project ID you want to modify **can edit only the title of project ** (Enter 0 to exit): ")
            if seleced_project_id == "0":
                break
            elif seleced_project_id in project_id_list:
                title = input('Enter/Modify title: ')
                project_table.update(["projectID"], [seleced_project_id], ["title"], [title])
                print(f"modify project ID: {seleced_project_id} successful")
                break
            else:
                print("***Project ID invalid please try again***")
    else:
        print("Project table not found")
        return


# DONE
def send_request_to_member(db, person_login):
    member_pending_requese_table = db.tables.get("member_pending")
    if member_pending_requese_table:
        project_id_list = get_all_project_id_of_lead(db, person_login.ID)
        while True:
            print(f"My project ID: {', '.join(project_id_list)}")
            project_id = input("Choose your project ID to send a request (Enter 0 to exit):")
            if project_id == "0":
                return
            elif project_id in project_id_list:
                break
            else:
                print("***Project ID invalid please try again***\n")
        while True:
            person_id = input("Enter student ID to send a request (Enter 0 to exit):")
            if person_id == "0":
                return
            elif search_person_by_id(db, person_id, "student"):
                break
            else:
                print("***Student ID invalid or this ID is not student, please try again***\n")

        insert_dict = {
            "projectID": project_id,
            "to_be_member": person_id,
            "response": "pending",
            "response_date": ""
            # "response_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # insert
        member_pending_requese_table.insert(insert_dict)
        print(f"request sent completed to student ID {person_id}!!")

    else:
        print("member pending request table not found")
        return


# DONE
def send_request_to_advisor(db, person_login):
    advisor_pending_request_table = db.tables.get("advisor_pending")
    if advisor_pending_request_table:
        project_id_list = get_all_project_id_of_lead(db, person_login.ID)
        while True:
            print(f"My project ID: {', '.join(project_id_list)}")
            project_id = input("Choose your project ID to send a request (Enter 0 to exit):")
            if project_id == "0":
                return
            elif project_id in project_id_list:
                if not is_project_pending_member(db, project_id):
                    break
                else:
                    print("***Project has pending member can't send request to advisor***\n")
            else:
                print("***Project ID invalid please try again***\n")
        while True:
            faculty_id = input("Enter advisor ID to send a request (Enter 0 to exit):")
            if faculty_id == "0":
                return
            elif search_person_by_id(db, faculty_id, "faculty"):
                break
            else:
                print("***faculty ID invalid or this ID is not faculty, please try again***\n")

        insert_dict = {
            "projectID": project_id,
            "to_be_advisor": faculty_id,
            "response": "pending",
            "response_date": ""
        }
        # insert
        advisor_pending_request_table.insert(insert_dict)
        update_project_status(db, project_id, "pending advisor")

        print(f"request sent completed to faculty ID {faculty_id}!!")

    else:
        print("advisor pending request table not found")
        return


def see_all_pending_request_for_advisor(db, person_login):
    advisor_pending_requese_table = db.tables.get("advisor_pending")
    if advisor_pending_requese_table:
        is_no_request = True
        print("List of all project request you to advise their team...")
        for pending in advisor_pending_requese_table.rows:
            if pending.to_be_advisor == person_login.ID and pending.response == "pending":
                project = search_project_by_id(db, pending.projectID)
                print(f"\t- ProjectID: {project.projectID}: Project {project.title}; status = ({project.status})")
                is_no_request = False
        if is_no_request:
            print("No any advisor request send to you.....!!!")
    else:
        print("advisor pending request table not found")
        return


def accept_advisor_request(db, person_login):
    advisor_pending_requese_table = db.tables.get("advisor_pending")
    if advisor_pending_requese_table:
        project_id_list = []
        print("List of all project request you to advise their team...")
        for pending in advisor_pending_requese_table.rows:
            if pending.to_be_advisor == person_login.ID and pending.response == "pending":
                project = search_project_by_id(db, pending.projectID)
                print(f"\t- ProjectID: {project.projectID}: Project {project.title}, status = ({project.status})")
                project_id_list.append(project.projectID)

        if len(project_id_list) == 0:
            print("No any advisor request send to you.....!!!")
            return

        while len(project_id_list) > 0:
            print()
            print(f"{len(project_id_list)} invitation remain...")
            seleced_project_id = input(
                "Choose project ID you want to accept or deny **can accept only one project** (Enter 0 to exit): ")
            if seleced_project_id == "0":
                break
            elif seleced_project_id in project_id_list:
                while True:
                    accept_flag = input("accept invitation of Project ID {seleced_project_id} (Y/n): ")
                    if accept_flag != "Y" and accept_flag != "n":
                        print("***Input invalid Please select only Y or n only***")
                    else:
                        if accept_flag == "Y":
                            advisor_pending_requese_table.update(["projectID", "to_be_advisor"],
                                                                 [seleced_project_id, person_login.ID],
                                                                 ["response", "response_date"],
                                                                 ["accept",
                                                                  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                                                                 )
                            update_login_role(db, person_login.ID, "advisor")
                            update_new_advisor_to_project(db, seleced_project_id, person_login.ID)
                            project_id_list.remove(seleced_project_id)

                            update_decline_advisor_by_project_list(db, project_id_list, person_login.ID)
                            project_id_list.clear()

                            print(f"accepted invitation of Project ID: {seleced_project_id}")
                            print("-----And decline invitation on other Project-----")
                        else:
                            advisor_pending_requese_table.update(["projectID", "to_be_advisor"],
                                                                 [seleced_project_id, person_login.ID],
                                                                 ["response", "response_date"],
                                                                 ["decline",
                                                                  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                                                                 )
                            project_id_list.remove(seleced_project_id)
                        break
            else:
                print("***Project ID invalid please try again***")
    else:
        print("advisor pending request table not found")
        return


def see_project_detail_for_advisor(db, person_login):
    project_table = db.tables.get("project")
    if project_table:
        for project in project_table.rows:
            if project.advisor == person_login.ID:
                print(f"- Project {project.title}; status = ({project.status})")
    else:
        print("project table not found")
        return


# DONE
def see_student_member_for_advisor(db, person_login):
    project_table = db.tables.get("project")
    if project_table:
        for project in project_table.rows:
            if project.advisor == person_login.ID:
                print_all_person_by_person_list(db, [project.lead, project.member1, project.member2], "member")
    else:
        print("project table not found")
        return


def exit(db):
    persons_table = db.tables.get('persons')
    login_table = db.tables.get('login')
    project_table = db.tables.get('project')
    advisor_pending_request_table = db.tables.get('advisor_pending')
    member_pending_requese_table = db.tables.get('member_pending')

    if persons_table:
        persons_table.write_csv()

    if login_table:
        login_table.write_csv()

    if project_table:
        project_table.write_csv()

    if advisor_pending_request_table:
        advisor_pending_request_table.write_csv()

    if member_pending_requese_table:
        member_pending_requese_table.write_csv()


db = initializing()
person_login = login(db)


if person_login.role == "admin":
    while True:
        print(f"Choose function for admin (ID: {person_login.ID})")
        print("1. See all project information")
        print("2. See all student information that didn't join any project")
        print("3. See all faculty information that didn't advise any project")
        print("4. See all member pending request")
        print("5. See all advisor pending request")
        print("0. Choose 0 for Exit program")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            see_all_project_information(db)
        elif choice == 2:
            see_all_student_no_project(db)
        elif choice == 3:
            see_all_faculty_no_project(db)
        elif choice == 4:
            see_all_member_pending_request(db)
        elif choice == 5:
            see_all_advisor_pending_request(db)
        elif choice == 0:
            print("Exit Program...!!")
            break
        else:
            print("Invalid choice please try agin with chioce (1,2,3,4,5 or 0)")
        print("\n")

elif person_login.role == "student":
    while True:
        print(f"Choose function for student (ID: {person_login.ID})")
        print("1. See all pending requests")
        print("2. Accept/deny the requests")
        print("3. Create a new project")
        print("0. Choose 0 for Exit program")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            see_all_pending_request_for_member(db, person_login)
        elif choice == 2:
            accept_member_request(db, person_login)
        elif choice == 3:
            create_project_by_student(db, person_login)
        elif choice == 0:
            print("Exit Program...!!")
            break
        else:
            print("Invalid choice please try agin with chioce (1,2,3 or 0)")
        print("\n")

elif person_login.role == "member":
    while True:
        print(f"Choose function for member (ID: {person_login.ID})")
        print("1. See project status")
        print("2. See and modify project information")
        print("3. See who has responded to the requests sent out")
        print("0. Choose 0 for Exit program")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            see_project_status(db, person_login)
        elif choice == 2:
            see_and_modify_project(db, person_login)
        elif choice == 3:
            see_responded_to_request_member(db, person_login)
        elif choice == 0:
            print("Exit Program...!!")
            break
        else:
            print("Invalid choice please try agin with chioce (1,2,3 or 0)")
        print("\n")

elif person_login.role == "lead":
    while True:
        print(f"Choose function for leader (ID: {person_login.ID})")
        print("1. See project status")
        print("2. See and modify project information")
        print("3. See who has responded to the requests sent out")
        print("4. Send out requests to potential members")
        print("5. Send out requests to a potential advisor")
        print("0. Choose 0 for Exit program")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            see_project_status(db, person_login)
        elif choice == 2:
            see_and_modify_project(db, person_login)
        elif choice == 3:
            see_responded_to_request_member(db, person_login)
        elif choice == 4:
            send_request_to_member(db, person_login)
        elif choice == 5:
            send_request_to_advisor(db, person_login)
        elif choice == 0:
            print("Exit Program...!!")
            break
        else:
            print("Invalid choice please try agin with chioce (1,2,3,4,5 or 0)")
        print("\n")

elif person_login.role == "faculty":
    while True:
        print(f"Choose function for faculty (ID: {person_login.ID})")
        print("1. See all pending requests")
        print("2. Accept/deny the requests")
        print("0. Choose 0 for Exit program")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            see_all_pending_request_for_advisor(db, person_login)
        elif choice == 2:
            accept_advisor_request(db, person_login)
        elif choice == 0:
            print("Exit Program...!!")
            break
        else:
            print("Invalid choice please try agin with chioce (1,2 or 0)")
        print("\n")

elif person_login.role == "advisor":
    while True:
        print(f"Choose function for advisor (ID: {person_login.ID})")
        print("1. See project detail, you advise")
        print("2. See all student detail, you advise")
        print("0. Choose 0 for Exit program")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            see_project_detail_for_advisor(db, person_login)
        elif choice == 2:
            see_student_member_for_advisor(db, person_login)
        elif choice == 0:
            print("Exit Program...!!")
            break
        else:
            print("Invalid choice please try agin with chioce (1,2 or 0)")
        print("\n")

exit(db)
