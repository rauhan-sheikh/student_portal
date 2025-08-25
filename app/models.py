from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password

# Custom user model
class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, "HOD"),
        (2, "Staff"),
        (3, "Student"),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, default=2)

    def __str__(self):
        return self.username

# Course model
class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Subject model
class Subject(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Staff model
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Staff: {self.admin.email}"


# Student model
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Student: {self.admin.email}"
