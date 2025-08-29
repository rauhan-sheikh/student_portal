from rest_framework import viewsets, generics, status
from .models import CustomUser, Staff, Student, Course, Subject
from .serializers import UserSerializer, StaffSerializer, StudentSerializer, CourseSerializer, SubjectSerializer, ProfileSerializer, PasswordChangeSerializer
from django.contrib.auth import get_user_model
from .permissions import isHOD, isStaff, isStudent, isHODorStaff,ReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, isHOD]

    def get_serializer_class(self):
        if self.action == "me":
            return ProfileSerializer
        if self.action == "change_password":
            return PasswordChangeSerializer
        return super().get_serializer_class()

    # Authenticated user can see their own profile
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user, context={"request": request})
        return Response(serializer.data)

    # Authenticated user can change their own password
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

