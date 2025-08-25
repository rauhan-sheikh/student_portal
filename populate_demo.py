import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_portal.settings')
django.setup()

from app.models import CustomUser, Staff, Student, Course, Subject

# Clear existing demo data

print("Deleting old demo data...")

Staff.objects.all().delete()
Student.objects.all().delete()
Course.objects.all().delete()
Subject.objects.all().delete()

# Create Courses

courses = []
course_names = ["Computer Science", "Electrical Engineering", "Mechanical Engineering"]
for name in course_names:
    c = Course.objects.create(name=name)
    courses.append(c)
print(f"Created courses: {[c.name for c in courses]}")

# Create Subjects

subjects = []
for c in courses:
    for sub_name in ["Math", "Physics", "Chemistry"]:
        s = Subject.objects.create(name=f"{sub_name} - {c.name}", course=c)
        subjects.append(s)
print(f"Created subjects: {[s.name for s in subjects]}")

# Create Staff

num_staff = 5
staff_list = []
for i in range(1, num_staff + 1):
    u = CustomUser.objects.create_user(
        username=f"staff{i}",
        email=f"staff{i}@example.com",
        password="staff1234",
        user_type="2"
    )
    s = Staff.objects.create(admin=u, address=f"Staff Address {i}")
    staff_list.append(s)
print(f"Created {num_staff} staff members.")


# Create Students

num_students = 10
student_list = []
for i in range(1, num_students + 1):
    c = random.choice(courses)
    u = CustomUser.objects.create_user(
        username=f"student{i}",
        email=f"student{i}@example.com",
        password="student1234",
        user_type="3"
    )
    s = Student.objects.create(admin=u, course=c, address=f"Student Address {i}")
    student_list.append(s)
print(f"Created {num_students} students.")

print("Demo population complete!")
