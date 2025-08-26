# Student Portal Backend

A **Django REST Framework** based backend for a Student Portal system that manages users, staff, students, courses, and subjects. This project provides APIs to perform CRUD operations on all entities, supports authentication with JWT tokens, and uses a custom user model.

This project is being improved **incrementally** toward production-ready quality

---

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [API Endpoints & Documentation](#api-endpoints--documentation)
- [Incremental Progress](#incremental-progress)
- [Future Scope / Potential Additions](#future-scope--potential-additions)

---

## Features

- Custom user model with roles (HOD, Staff, Student)
- JWT authentication with refresh tokens
- CRUD APIs for users, staff, students, courses, and subjects
- Admin interface for model management
- Interactive API documentation (Swagger UI & ReDoc)

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/rauhan-sheikh/student_portal.git
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
pip install -r requirements.txt
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

## API Endpoints & Documentation

Here are the main categories of APIs (full details are available in the generated docs).

### Authentication

- `POST /api/auth/token/` – Obtain JWT token
- `POST /api/auth/token/refresh/` – Refresh JWT token

### Users

- `GET /api/users/` – List all users
- `POST /api/users/` – Create a new user

### Staff

- `GET /api/staff/` – List staff
- `POST /api/staff/` – Create staff

### Students

- `GET /api/students/` – List students
- `POST /api/students/` – Create student

### Courses

- `GET /api/courses/` – List courses
- `POST /api/courses/` – Create course

### Subjects

- `GET /api/subjects/` – List subjects
- `POST /api/subjects/` – Create subject

### API Schema & Documentation

- `GET /api/schema/` – OpenAPI schema (JSON/YAML)
- `GET /api/docs/swagger/` – Swagger UI (interactive docs)
- `GET /api/docs/redoc/` – ReDoc (alternative API docs)  
  Use these docs to explore all available endpoints interactively.

---

## Incremental Progress

This project is under active development, with improvements added step by step:

✅ Iteration 1: CRUD APIs with JWT auth

✅ Iteration 2: Interactive API documentation (Swagger & ReDoc)

🔄 Next: User registration flow, role-based permissions, and testing

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
