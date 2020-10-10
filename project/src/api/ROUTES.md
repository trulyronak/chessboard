# Routes

## ***Notes***

- List any routes you want us to add/change here.
- Also bugs lol but mucho changed recently so a lot of routes are broken rn but they'll be fixed soon

# Doc for API Routes and Usages

## ***Enrolled_Course***
(Prefix = enrolled_course)
### **enroll_user (POST)**
#### *Description*
Route to enroll a user in to a specific section of a course. 

#### *Parameters*
- **user_id: int** --> The id of the user to enroll.
- **section_id: int** --> The section_id of the course to enroll user in.
- **course_id: int** --> The course_id of the course to enroll user in.
- **role (optional): string** --> The role of the enrolled user in the course, default is set to be student. Candidates: ROOT, ADMIN, INSTRUCTOR, GRADER, STUDENT.

#### *Responses*
- **{'reason': 'user enrolled}, 200** when the request success.
- **{'reason': 'user existed}, 400** when the request failed due to a user is already enrolled.


### **change_role (POST)**
#### *Description*
Route to change the role of an already enrolled user in a specific course.

#### *Parameters*
- **user_id: int** --> The id of the user to change role.
- **course_id: int** --> The course_id of the course to change the role of the user in.
- **role: string** --> The role of the enrolled user in the course. Candidates: ROOT, ADMIN, INSTRUCTOR, GRADER, STUDENT.

#### *Responses*
- **{'reason': 'Role changed'}, 200** when role is successfully changed.
- **{'reason': ' User not enrolled'}, 400** when the user is not enrolled in the course.


### **delete_user_from_course (POST)**
#### *Description*
HARD delete a user from a course that one enrolled.

#### *Parameters*
- **user_id: int** --> The id of the user to be deleted.
- **course_id: int** --> The course_id of the course to delete the user from.

#### *Responses*
- **{'reason': 'user deleted'}, 200** when the user is successfully deleted.
- **{'reason': 'user not found'}, 400** when the user is not found in the course.

### **get_user_of_course (GET) **
#### *Description*
Get the enrolled_course information of a user in a course.

#### *Parameters*
- **user_id: int** --> The id of the user to be searched.
- **course_id: int** --> The course_id of the course to be searched.

#### *Responses*
- **{'reason': 'success', 'result': ret}, 200** where **ret** consists of the following:
```python
ret = {
    'user_info': {
        'fname': 'The first name of the user'
        'lname': 'The last name of the user'
        'email': 'The email of the user'
        'id': 'The id of the user'
        'pid': 'The pid of the user'
        'last_login': 'Time stamp of the last time this user logged in'
    }
    'enrolled_course_info': {
        'user_id': 'The user_id of the enrolled_course entry'
        'course_id': 'The course id of this enrolled_course entry'
        'section_id': 'The section id of this enroleld_course entry'
        'id': 'The id of this enrolled_course entry'
        'status': 'The status of this enrolled_course entry (for tutor avalibilities)'
        'role' : 'The role of this enrolled_course entry'
    }
}
```

### **get_all_user_in_course (GET)**
#### *Description*
Get all the users in a given course (with certain role).

#### *Parameters*
- **course_id: int** --> The course_id of the course to search for.
- **roles: string** --> A colon seperated list of strings of all the roles to search for. Candidates: ROOT, ADMIN, INSTRUCTOR, GRADER, STUDENT.

#### *Responses*
- **{'reason': 'success', 'result': ret}, 200** where **ret** is
```python
ret = [{
    'user_info': {
        'fname': 'The first name of the user'
        'lname': 'The last name of the user'
        'email': 'The email of the user'
        'id': 'The id of the user'
        'pid': 'The pid of the user'
        'last_login': 'Time stamp of the last time this user logged in'
    }
    'enrolled_user_info': {
        'user_id': 'The user_id of the enrolled_course entry'
        'course_id': 'The course id of this enrolled_course entry'
        'section_id': 'The section id of this enroleld_course entry'
        'id': 'The id of this enrolled_course entry'
        'status': 'The status of this enrolled_course entry (for tutor avalibilities)'
        'role' : 'The role of this enrolled_course entry'
    }
}]
```
- **{'reason': 'course not found'}, 400** when failed.

### **get_user_in_section (GET)**
#### *Description*
Get all the users in a given section.

#### *Parameters*
- **course_id: int** --> The course_id of the course to search for.
- **section_id: int** --> The section_id of the section to search for.

#### *Responses*
- **{'reason': 'success', 'result': ret}, 200** where **ret** is
```python
ret = [{
    'user_info': {
        'fname': 'The first name of the user'
        'lname': 'The last name of the user'
        'email': 'The email of the user'
        'id': 'The id of the user'
        'pid': 'The pid of the user'
        'last_login': 'Time stamp of the last time this user logged in'
    }
    'enrolled_user_info': {
        'user_id': 'The user_id of the enrolled_course entry'
        'course_id': 'The course id of this enrolled_course entry'
        'section_id': 'The section id of this enroleld_course entry'
        'id': 'The id of this enrolled_course entry'
        'status': 'The status of this enrolled_course entry (for tutor avalibilities)'
        'role' : 'The role of this enrolled_course entry'
    }
}]
```


### **get_courses_user_in (GET)**
#### *Description*
Get all the courses a user is in.

#### *Parameters*
- **user_id: int** --> The id of the user to saerch for.
- **roles: string** --> A colon seperated list of strings of all the roles to search for. Candidates: ROOT, ADMIN, INSTRUCTOR, GRADER, STUDENT.

#### *Responses*
- **'reason': 'success', 'result': ret}), 200** where **ret** is
```python
ret = {
    'user_info': {
        'fname': 'The first name of the user'
        'lname': 'The last name of the user'
        'email': 'The email of the user'
        'id': 'The id of the user'
        'pid': 'The pid of the user'
        'last_login': 'Time stamp of the last time this user logged in'
    }
    'courses': [{
        'user_id': 'The user_id of the enrolled_course entry'
        'course_id': 'The course id of this enrolled_course entry'
        'section_id': 'The section id of this enroleld_course entry'
        'id': 'The id of this enrolled_course entry'
        'status': 'The status of this enrolled_course entry (for tutor avalibilities)'
        'role' : 'The role of this enrolled_course entry'
    }]
}

```

### **find_active_tutor_for (GET)**
#### *Description*
Get all the active tutor of a queue.

#### *Parameters*
- **queue_id: int** --> The id of the queue to search for.


## ***Ticket API***

### **add_ticket (POST)**

#### *Description*

Adds a ticket to the queue. 

#### *Parameters*

- **queue_id: int** id of queue ticket is on
- **student_id: int** id of student who added the ticket
- **title: string** title of ticket
- **description: string** description of ticket
- **room: string** room where ticket was added
- **workstation: string** workstation ticket was added on
- **is_private: int** whether the ticket is private. pass in 0 or 1
- **help_type: string** help type. see ../models/ticket.py for help types
- **tag_list: string** list of tags associated with tickets. pass in semi-colon separated list. see ../models/ticket.py for ticket tags

### **get_info (GET)**

#### *Description*

Get all of a ticket's properties in json format.

#### *Parameters*

- **user_id: int** id of user requesting to view ticket info
- **ticket_id: int** id of ticket

### **get_user_permissions (GET)**

#### *Description*

Determines if a user can view or edit a ticket

#### *Parameters*

- **user_id: int** id of user whose permissions are being checked
- **ticket_id: int** id of ticket





