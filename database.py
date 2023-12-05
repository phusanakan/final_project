import csv, os

# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
# persons = []
# with open(os.path.join(__location__, 'persons.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         persons.append(dict(r))
# print(persons)

# add in code for a Database class


class Database:
    def __init__(self):
        self.tables = {}

    def add_table(self, table_name, file_path, row_class=None):
        table = Table(file_path, row_class)
        table.read_csv()
        self.tables[table_name] = table # add new table to database tables dict
        return self.tables[table_name].rows



class Table:
    def __init__(self, file_path, row_class=None):
        self.file_path = file_path
        self.row_class = row_class
        self.rows = []

    def read_csv(self): # load data from csv
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                rows = csv.DictReader(f)
                for r in rows:
                    if self.row_class:
                        self.rows.append(self.row_class(**r))
                    else:
                        self.rows.append(dict(r))

    def write_csv(self): # save whole new data to csv
        with open(self.file_path, 'w', newline='') as f:
            fieldnames = self.rows[0].keys() if self.rows else []
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.rows)

    def insert(self, entry):
        if self.row_class:
            self.rows.append(self.row_class(**entry))
        else:
            self.rows.append(entry)

    def update(self, entry_id_key_list, entry_id_list, update_key_list, update_value_list):
        for i in range(len(self.rows)):
            entry = self.rows[i].__dict__

            if len(entry_id_key_list) != len(entry_id_list):
                print("entry_id_key_list and entry_id_list size not match (Can't update)")
                break

            is_update_row = True
            for j in range(len(entry_id_key_list)):
                if entry[entry_id_key_list[j]] != entry_id_list[j]:
                    is_update_row = False

            if is_update_row:
                if len(update_key_list) != len(update_value_list):
                    print("update_key_list and update_value_list size not match (Can't update)")
                    break
                for j in range(len(update_key_list)):
                    entry[update_key_list[j]] = update_value_list[j]
                self.rows[i] = self.row_class(**entry)
                break


class Login:
    def __init__(self, ID, username, password, role):
        self.ID = ID
        self.username = username
        self.password = password
        self.role = role


class Project:
    def __init__(self, projectID, title, lead, member1, member2, advisor, status):
        self.projectID = projectID
        self.title = title
        self.lead = lead
        self.member1 = member1
        self.member2 = member2
        self.advisor = advisor
        self.status = status


class AdvisorPendingRequest:
    def __init__(self, ProjectID, to_be_advisor, response, response_date):
        self.ProjectID = ProjectID
        self.to_be_advisor = to_be_advisor
        self.response = response
        self.response_date = response_date


class MemberPendingRequest:
    def __init__(self, projectID, to_be_member, response, response_date):
        self.projectID = projectID
        self.to_be_member = to_be_member
        self.response = response
        self.response_date = response_date


class Person:
    def __init__(self, ID, first, last, type):
        self.ID = ID
        self.first = first
        self.last = last
        self.type = type

    def view_invitation(self, sender, project):
        print(f"{self.first} {self.first}, you received an invitation from {sender.first_name} {sender.last_name} "
              f"for project {project.project_id}.")

    def respond_to_invitation(self, sender, project, response):
        if response.lower() == 'accept':
            print(f"{self.first} {self.first} accepted the invitation for project {project.project_id}.")
        elif response.lower() == 'deny':
            print(f"{self.first} {self.first} denied the invitation for project {project.project_id}.")
        else:
            print("Invalid response. Please enter 'accept' or 'deny'.")

    def view_project_details(self):
        print(f"{self.first} {self.first}, here are the details of your project:")


class Student(Person):
    def __init__(self, person_id, first_name, last_name):
        super().__init__(person_id, first_name, last_name, 'student')

    def join_project(self, lead, project):
        print(f"{self.first_name} {self.last_name} joined project {project.project_id} led by {lead.first_name} {lead.last_name}.")


    def send_invitation(self, member, project):
        print(f"{self.first_name} {self.last_name} sent an invitation to {member.first_name} {member.last_name} "
              f"for project {project.project_id}.")


class Faculty(Person):
    def __init__(self, person_id, first_name, last_name):
        super().__init__(person_id, first_name, last_name, 'faculty')

    def respond_to_request(self, student, project):
        pass

    def view_all_projects(self):
        pass

    def evaluate_project(self, project):
        pass


class Admin(Person):
    def __init__(self, person_id, first_name, last_name):
        super().__init__(person_id, first_name, last_name, 'admin')

    def manage_database(self):
        pass


class SeniorProject:
    def __init__(self, project_id, lead, members, advisor, proposal_status, report_status, evaluation_status):
        self.project_id = project_id
        self.lead = lead
        self.members = members
        self.advisor = advisor
        self.proposal_status = proposal_status
        self.report_status = report_status
        self.evaluation_status = evaluation_status

    def submit_proposal(self, proposal):
        print(f"Project {self.project_id} submitted a proposal: {proposal}")

    def submit_report(self, report):
        print(f"Project {self.project_id} submitted the final report: {report}")


class Evaluation:
    def __init__(self, evaluation_id, evaluator, project, comments, score):
        self.evaluation_id = evaluation_id
        self.evaluator = evaluator
        self.project = project
        self.comments = comments
        self.score = score

    def provide_feedback(self, comments):
        print(f"Evaluator {self.evaluator.first_name} {self.evaluator.last_name} provided feedback on project {self.project.project_id}: {comments}")

    def assign_score(self, score):
        print(
            f"Evaluator {self.evaluator.first_name} {self.evaluator.last_name} assigned a score of {score} to project {self.project.project_id}.")

