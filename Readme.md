# Student Portal Backend

A **Django REST Framework** based backend for a Student Portal system that manages users, staff, students, courses, and subjects. This project provides APIs to perform CRUD operations on all entities, supports authentication with JWT tokens, and uses a custom user model.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Future Scope / Potential Additions](#future-scope--potential-additions)

---

## Project Structure

```
.
├── app                  # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py        # Custom user, student, staff, course, subject models
│   ├── serializers.py   # DRF serializers for models
│   ├── urls.py          # Application-level URL routing
│   ├── views.py         # API viewsets
│   └── migrations/
├── student_portal       # Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── db.sqlite3           # SQLite database
├── manage.py
└── populate_demo.py     # Script to populate demo data (optional)
```

---

## Features

- **Custom User Model** (`CustomUser`) with roles:
  - HOD
  - Staff
  - Student
- **CRUD APIs** for:
  - Users
  - Staff
  - Students
  - Courses
  - Subjects
- **JWT-based Authentication** using `rest_framework_simplejwt`
- Separate models for **Staff** and **Students** linked to `CustomUser`
- Each student is associated with a \*\*Course`
- Admin interface support for managing models

---

## Setup Instructions

1. Clone the repository:

```bash
git clone <repo-url>
cd student_portal
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

---

## API Endpoints

- **Authentication**

  - `POST /api/auth/token/` – Obtain JWT token
  - `POST /api/auth/token/refresh/` – Refresh JWT token

- **Users**

  - `GET /api/users/` – List all users
  - `POST /api/users/` – Create user
  - `GET /api/users/{id}/` – Retrieve user
  - `PUT /PATCH /api/users/{id}/` – Update user
  - `DELETE /api/users/{id}/` – Delete user

- **Staff**

  - `GET /api/staff/` – List staff
  - `POST /api/staff/` – Create staff
  - `GET /api/staff/{id}/` – Retrieve staff
  - `PUT /PATCH /api/staff/{id}/` – Update staff
  - `DELETE /api/staff/{id}/` – Delete staff

- **Students**

  - `GET /api/students/` – List students
  - `POST /api/students/` – Create student
  - `GET /api/students/{id}/` – Retrieve student
  - `PUT /PATCH /api/students/{id}/` – Update student
  - `DELETE /api/students/{id}/` – Delete student

- **Courses**

  - `GET /api/courses/` – List courses
  - `POST /api/courses/` – Create course
  - `GET /api/courses/{id}/` – Retrieve course
  - `PUT /PATCH /api/courses/{id}/` – Update course
  - `DELETE /api/courses/{id}/` – Delete course

- **Subjects**
  - `GET /api/subjects/` – List subjects
  - `POST /api/subjects/` – Create subject
  - `GET /api/subjects/{id}/` – Retrieve subject
  - `PUT /PATCH /api/subjects/{id}/` – Update subject
  - `DELETE /api/subjects/{id}/` – Delete subject

All endpoints follow standard **CRUD operations** via **Django REST Framework ViewSets**.

---

## Authentication

This project uses **JWT (JSON Web Tokens)** for authentication. Tokens can be obtained using:

```json
POST /api/auth/token/
{
  "username": "admin",
  "password": "password"
}
```

Use the returned `access` token in the `Authorization` header for API requests:

```
Authorization: Bearer <access_token>
```

---

## Future Scope / Potential Additions

1. **Role-Based Permissions**
   - Limit access for students, staff, and HODs to specific endpoints.
2. **Attendance Management**

   - Track student attendance with daily logs.

3. **Exams & Results**

   - Add models for exams, grades, and results.
   - APIs for teachers to upload results and students to view them.

4. **Notifications**

   - Email or in-app notifications for events like result declaration or announcements.

5. **Frontend Integration**

   - React.js or Angular frontend for a complete student portal.

6. **Profile Pictures**

   - Allow uploading profile pictures for students and staff.

7. **Search & Filters**

   - Search students by course, name, or email.
   - Filter subjects by course.

8. **Audit Logs**

   - Keep track of changes made by users (admin/staff).

9. **Deployment**

   - Prepare for deployment using **Docker**, **NGINX**, and **PostgreSQL**.

10. **Analytics**
    - Track student performance trends, attendance stats, etc.

---

This backend provides a **strong foundation** for a fully functional student portal and can be extended with more **academic features**, **role-based access**, and **analytics dashboards** in the future.
