from rest_framework import viewsets
from .models import CustomUser, Staff, Student, Course, Subject
from .serializers import UserSerializer, StaffSerializer, StudentSerializer, CourseSerializer, SubjectSerializer
from django.contrib.auth import get_user_model
from .permissions import isHOD, isStaff, isStudent, isHODorStaff,ReadOnly
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, isHOD]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, isHODorStaff]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 3:  # student
            return Student.objects.filter(admin=user)
        return super().get_queryset()


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 3:  # If the user is a student
            try:
                return Course.objects.filter(id=user.student.course.id)
            except Student.DoesNotExist:
                return Course.objects.none()
        return super().get_queryset()


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 3:  # If the user is a student
            try:
                return Subject.objects.filter(course=user.student.course)
            except Student.DoesNotExist:
                return Subject.objects.none()
        return super().get_queryset()
