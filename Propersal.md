**Proposal**

Module 1: database.py
Objective:
The database.py module manages data behind the scenes. It does things like keeping track of users, projects, and requests. Key objectives include:

Initialization:

Sets up the database and loads existing data.
User and Project Data:

Manages user details (students, faculty) and project information.
Pending Requests:

Handles pending requests for project membership or advisor assistance.
Data Saving:

Writes changes back to files for data storage.
Usage:
It works quietly in the background, making sure data is organized and up-to-date.

Module 2: project_manage.py
Objective:
The project_manage.py module is what users interact with directly. It does the following:

Login and Setup:

Helps users log in and gets everything ready.
Admin Features:

Admin can check all project info and see who needs teams.
Student Features:

Students manage requests and create new projects.
Team Member Features:

Team members view and modify project details.
Team Lead Features:

Team leads manage projects and invite new members.
Faculty and Advisor Features:

Faculty manage requests and see details of advised projects.
Exit Function:

Saves changes made during the session.
Usage:
Users pick options from a menu to do different tasks based on their role.

This simplified proposal highlights the main goals and functionalities of the Academic Project Management System, making it easy for a first-year student to understand.