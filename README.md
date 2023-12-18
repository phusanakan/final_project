# Project Management System

This project implements a comprehensive Project Management System with various roles, including Admin, Student, Member, Lead, Advisor, Faculty, and relevant functionalities for each role.

## Files

### database.py

- **Database Class:** Used for storing Table objects.
- **Table Class:** Stores data read from CSV files.
- Various "quality of life" functions for easier interaction with project_manage.py.

### project_manage.py

- Contains classes for each role, including the `Performance` class that utilizes the value returned from the `login()` function to perform role-specific activities.

### persons.csv

- Contains information about all individuals involved in the system.

### login.csv

- Contains information necessary for login.

### Project_table.csv

- Contains all project information. Initially empty; only header provided.

### Member_pending_request.csv

- Contains all history of requests to be a member. Initially empty; only header provided.

### Advisor_pending_request.csv

- Contains all history of requests to be an advisor. Initially empty; only header provided.

## Usage

1. Run the program.
2. Log in with your credentials.

## Role-Specific Actions

### Admin Role

- See all project information.
- See all students not associated with any project.
- See all faculty members not advising any project.
- See all pending member requests.
- See all pending advisor requests.

### Student Role

- See all pending requests.
- Accept/deny requests.
- Create a new project.

### Member Role

- See project status.
- See and modify project information.
- See who has responded to the requests sent out.

### Lead Role

- See project status.
- See and modify project information.
- See who has responded to the requests sent out.
- Send out requests to potential members.
- Send out requests to a potential advisor.

### Advisor Role

- See all pending requests.
- Accept/deny requests.

### Faculty Role

- See project details for advised projects.
- See all student details for advised projects.

## Completion

Everything in the program is 100% complete.

## Missing Features

- No missing features; the program is complete.

## Bug

- No bugs identified in the program.


