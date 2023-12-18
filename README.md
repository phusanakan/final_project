# Project README

## Overview
Brief description of your project.

## Repository Contents
- `database.py`: Contains classes `Database` and `Table` for storing data and facilitating database operations.
- `project_manage.py`: Main script containing classes for each role, and activities related to each role.
- `persons.csv`: CSV file containing information about all persons.
- `login.csv`: CSV file containing information necessary for login.
- `Project_table.csv`: CSV file containing project information (Initially empty, only header given).
- `Member_pending_request.csv`: CSV file containing the history of requests to be a member (Initially empty, only header given).
- `Advisor_pending_request.csv`: CSV file containing the history of requests to be an advisor (Initially empty, only header given).

## Files and Classes

### `database.py`
1. **Database:** Class for storing `Table` objects.
   - Methods:
     - `__init__(self)`: Constructor to initialize a `Database` instance.
     - ...

2. **Table:** Class for storing data read from CSV files.
   - Methods:
     - `__init__(self, table_name, columns)`: Constructor to initialize a `Table` instance.
     - ...

3. Other "quality of life" functions included for easier work on `project_manage.py`.

### `project_manage.py`
1. **Performance:** Class using the value returned from `login()` function to perform activities of each role.
   - Methods:
     - `__init__(self, database)`: Constructor to initialize a `Performance` instance.
     - ...

2. Classes for each role (Student, Lead, Advisor, Faculty, Admin), each containing activities related to that role.
   - Methods:
     - Methods for actions specific to each role, e.g., checking project invitations, sending requests, etc.


**Roles and Actions**

_Student Role_

| Action                               | Relevant Classes/Methods                        |
|--------------------------------------|------------------------------------------------|
| Check project invitations            | `check_project_invitations()`                   |
| Create project                       | `create_project()`                              |
| Check project status                 | `check_project_status()`                        |
| Edit project details                 | `edit_project_details()`                        |
| Submit project                       | `submit_project()`                              |
| Cancel project                       | `cancel_project()`                              |
| Logout                               | `logout()`                                      |

_Member Role_

| Action                         | Relevant Classes/Methods               |
|--------------------------------|---------------------------------------|
| Check Project Invitations      | `check_project_invitations()`          |
| Create Project                 | `create_project()`                     |
| Check Project Status           | `check_project_status()`               |
| Edit Project Details           | `edit_project_details()`               |
| Submit Project                 | `submit_project()`                     |
| Cancel Project                 | `cancel_project()`                     |
| Logout                         | `logout()`                             |


| Action                               | Relevant Classes/Methods                        |
|--------------------------------------|------------------------------------------------|
| Check project invitations            | `check_project_invitations()`                   |
| Create project                       | `create_project()`                              |
| Check project status                 | `check_project_status()`                        |
| Edit project details                 | `edit_project_details()`                        |
| Submit project                       | `submit_project()`                              |
| Cancel project                       | `cancel_project()`                              |
| Logout                               | `logout()`                                      |

_Lead Role_

| Action                               | Relevant Classes/Methods                        |
|--------------------------------------|------------------------------------------------|
| Check project invitations            | `check_project_invitations()`                   |
| Create project                       | `create_project()`                              |
| Check project status                 | `check_project_status()`                        |
| Send member requests                 | `send_member_request()`                         |
| Send advisor requests                | `send_advisor_request()`                        |
| Submit project                       | `submit_project()`                              |
| Cancel project                       | `cancel_project()`                              |
| Logout                               | `logout()`                                      |

_Advisor Role_

| Action                               | Relevant Classes/Methods                        |
|--------------------------------------|------------------------------------------------|
| Check project invitations            | `check_project_invitations()`                   |
| Accept/deny advisor requests         | `accept_advisor_request()`                      |
| See project details                  | `see_project_details()`                         |
| See student member details           | `see_student_member_details()`                  |
| Submit project                       | `submit_project()`                              |
| Cancel project                       | `cancel_project()`                              |
| Logout                               | `logout()`                                      |

_Faculty Role_


| Action                               | Relevant Classes/Methods                        |
|--------------------------------------|------------------------------------------------|
| Check project requests               | `check_project_requests()`                      |
| See projects for approval            | `see_projects_for_approval()`                   |
| See all student details              | `see_all_student_details()`                     |
| Submit project                       | `submit_project()`                              |
| Cancel project                       | `cancel_project()`                              |
| Logout                               | `logout()`                                      |

_Admin Role_

| Action                               | Relevant Classes/Methods                        |
|--------------------------------------|------------------------------------------------|
| Check all projects information       | `see_all_project_information()`                 |
| See member and faculty details        | `see_all_student_no_project()`                  |
| See all member pending requests       | `see_all_member_pending_request()`              |
| Check all advisor pending requests    | `see_all_advisor_pending_request()`            |
| Check canceled projects              | `check_canceled_projects()`                     |
| Logout                               | `logout()`                                      |

Completion in %: 100%

Missing Features
-

Bug
-